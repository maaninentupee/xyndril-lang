"""
Xyndril Interpreter Design

This module defines the interpreter for the Xyndril language.
The interpreter traverses the AST and executes the program.
"""

class Environment:
    """Represents a variable scope environment"""
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent
    
    def define(self, name, value):
        """Define a variable in the current environment"""
        self.variables[name] = value
        return value
    
    def lookup(self, name):
        """Look up a variable in the environment chain"""
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.lookup(name)
        raise NameError(f"Variable '{name}' is not defined")
    
    def assign(self, name, value):
        """Assign a new value to an existing variable"""
        if name in self.variables:
            self.variables[name] = value
            return value
        if self.parent:
            return self.parent.assign(name, value)
        raise NameError(f"Cannot assign to undefined variable '{name}'")

class RouteRegistry:
    """Manages the REST API routes defined in the program"""
    def __init__(self):
        self.routes = {}  # Dict of method -> Dict of path -> handler function
    
    def register(self, method, path, handler):
        """Register a new route handler"""
        if method not in self.routes:
            self.routes[method] = {}
        self.routes[method][path] = handler
        return handler
    
    def get_routes(self):
        """Return all registered routes"""
        return self.routes

class ClassRegistry:
    """Manages class definitions in the program"""
    def __init__(self):
        self.classes = {}
    
    def register(self, name, class_def):
        """Register a class definition"""
        self.classes[name] = class_def
        return class_def
    
    def get_class(self, name):
        """Get a class definition by name"""
        if name not in self.classes:
            raise NameError(f"Class '{name}' is not defined")
        return self.classes[name]

class Interpreter:
    """Xyndril language interpreter"""
    def __init__(self):
        self.global_env = Environment()
        self.route_registry = RouteRegistry()
        self.class_registry = ClassRegistry()
    
    def evaluate(self, node, env=None):
        """Evaluate an AST node"""
        if env is None:
            env = self.global_env
            
        # Dispatcher based on node type
        method_name = f"evaluate_{node.__class__.__name__}"
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method(node, env)
        else:
            raise NotImplementedError(f"Evaluation not implemented for {node.__class__.__name__}")
    
    # --- Expression evaluation methods ---
    
    def evaluate_Literal(self, node, env):
        """Evaluate a literal value"""
        return node.value
    
    def evaluate_Identifier(self, node, env):
        """Evaluate a variable reference"""
        return env.lookup(node.name)
    
    def evaluate_BinaryOperation(self, node, env):
        """Evaluate a binary operation"""
        left = self.evaluate(node.left, env)
        right = self.evaluate(node.right, env)
        
        if node.operator == "+":
            return left + right
        elif node.operator == "-":
            return left - right
        elif node.operator == "*":
            return left * right
        elif node.operator == "/":
            return left / right
        elif node.operator == "==":
            return left == right
        elif node.operator == "!=":
            return left != right
        elif node.operator == "<":
            return left < right
        elif node.operator == "<=":
            return left <= right
        elif node.operator == ">":
            return left > right
        elif node.operator == ">=":
            return left >= right
        else:
            raise ValueError(f"Unknown binary operator: {node.operator}")
    
    def evaluate_UnaryOperation(self, node, env):
        """Evaluate a unary operation"""
        expr = self.evaluate(node.expression, env)
        
        if node.operator == "-":
            return -expr
        elif node.operator == "!":
            return not expr
        else:
            raise ValueError(f"Unknown unary operator: {node.operator}")
    
    def evaluate_FunctionCall(self, node, env):
        """Evaluate a function call"""
        callee = self.evaluate(node.callee, env)
        args = [self.evaluate(arg, env) for arg in node.arguments]
        
        if callable(callee):
            return callee(*args)
        else:
            raise TypeError(f"'{callee}' is not callable")
    
    def evaluate_MemberExpression(self, node, env):
        """Evaluate a member expression (obj.prop)"""
        obj = self.evaluate(node.object, env)
        return getattr(obj, node.property)
    
    def evaluate_ArrowFunction(self, node, env):
        """Evaluate an arrow function expression"""
        def fn(*args):
            # Create a new environment with the parent being the lexical environment
            function_env = Environment(env)
            
            # Bind parameters to arguments
            for i, param in enumerate(node.parameters):
                if i < len(args):
                    function_env.define(param.name, args[i])
                elif param.default_value is not None:
                    function_env.define(param.name, self.evaluate(param.default_value, env))
                else:
                    raise TypeError(f"Missing required argument '{param.name}'")
            
            # If body is a block statement, execute it
            if hasattr(node.body, 'body'):
                result = None
                for stmt in node.body.body:
                    result = self.evaluate(stmt, function_env)
                    if isinstance(stmt, ReturnStatement):
                        return result
                return result
            else:
                # Body is a single expression
                return self.evaluate(node.body, function_env)
        
        return fn
    
    # --- Statement evaluation methods ---
    
    def evaluate_Program(self, node, env):
        """Evaluate a complete program"""
        result = None
        for stmt in node.body:
            result = self.evaluate(stmt, env)
        return result
    
    def evaluate_LetStatement(self, node, env):
        """Evaluate a variable declaration"""
        value = None
        if node.initializer:
            value = self.evaluate(node.initializer, env)
        return env.define(node.identifier.name, value)
    
    def evaluate_IfStatement(self, node, env):
        """Evaluate an if statement"""
        test_result = self.evaluate(node.test, env)
        
        if test_result:
            return self.evaluate(node.consequent, env)
        elif node.alternate:
            return self.evaluate(node.alternate, env)
        
        return None
    
    def evaluate_BlockStatement(self, node, env):
        """Evaluate a block statement"""
        result = None
        block_env = Environment(env)
        
        for stmt in node.body:
            result = self.evaluate(stmt, block_env)
            if isinstance(stmt, ReturnStatement):
                break
                
        return result
    
    def evaluate_ReturnStatement(self, node, env):
        """Evaluate a return statement"""
        if node.argument:
            return self.evaluate(node.argument, env)
        return None
    
    def evaluate_ExpressionStatement(self, node, env):
        """Evaluate an expression statement"""
        return self.evaluate(node.expression, env)
    
    # --- Class-related evaluation methods ---
    
    def evaluate_ClassDeclaration(self, node, env):
        """Evaluate a class declaration"""
        # Create a class definition object
        class_def = {
            'name': node.name.name,
            'properties': {},
            'methods': {},
            'constructor': None
        }
        
        # Process properties
        for prop in node.properties:
            class_def['properties'][prop.name.name] = None
        
        # Process methods
        for method in node.methods:
            method_fn = self.evaluate_ArrowFunction(
                ArrowFunction(method.parameters, method.body, method.return_type),
                env
            )
            class_def['methods'][method.name.name] = method_fn
        
        # Process constructor if present
        if node.constructor:
            constructor_fn = self.evaluate_ArrowFunction(
                ArrowFunction(node.constructor.parameters, node.constructor.body),
                env
            )
            class_def['constructor'] = constructor_fn
        
        # Register the class
        self.class_registry.register(node.name.name, class_def)
        
        # Define class constructor in the environment
        def class_constructor(*args):
            instance = {
                '__class__': node.name.name,
                '__data__': {}
            }
            
            # Initialize properties
            for prop_name in class_def['properties']:
                instance['__data__'][prop_name] = None
            
            # Add methods to instance
            for method_name, method_fn in class_def['methods'].items():
                def bound_method(*method_args):
                    return method_fn(instance, *method_args)
                instance[method_name] = bound_method
            
            # Call constructor if present
            if class_def['constructor']:
                class_def['constructor'](instance, *args)
            
            return instance
        
        env.define(node.name.name, class_constructor)
        return class_constructor
    
    # --- Route-related evaluation methods ---
    
    def evaluate_RouteDefinition(self, node, env):
        """Evaluate a route definition"""
        # Create a handler function for this route
        def route_handler(*args):
            # Create a new environment for the route
            route_env = Environment(env)
            
            # Execute the route body
            return self.evaluate(node.body, route_env)
        
        # Register the route
        self.route_registry.register(node.method, node.path, route_handler)
        return route_handler
