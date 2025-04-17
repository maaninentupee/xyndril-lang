# src/interpreter.py
# CoreFlux Interpreter: Evaluates AST produced by parser
from .ast import *

class Environment:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent
    def define(self, name, value):
        self.variables[name] = value
        return value
    def lookup(self, name):
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.lookup(name)
        raise NameError(f"Variable '{name}' is not defined")
    def assign(self, name, value):
        if name in self.variables:
            self.variables[name] = value
            return value
        if self.parent:
            return self.parent.assign(name, value)
        raise NameError(f"Cannot assign to undefined variable '{name}'")

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
    def evaluate(self, node, env=None):
        if env is None:
            env = self.global_env
        method_name = f"eval_{node.__class__.__name__}"
        if hasattr(self, method_name):
            return getattr(self, method_name)(node, env)
        raise NotImplementedError(f"No eval method for {node.__class__.__name__}")
    def eval_Program(self, node, env):
        result = None
        for stmt in node.body:
            result = self.evaluate(stmt, env)
        return result
    def eval_Literal(self, node, env):
        return node.value
    def eval_Identifier(self, node, env):
        return env.lookup(node.name)
    def eval_LetStatement(self, node, env):
        value = self.evaluate(node.initializer, env) if node.initializer else None
        return env.define(node.identifier.name, value)
    def eval_IfStatement(self, node, env):
        if self.evaluate(node.test, env):
            return self.evaluate(node.consequent, env)
        elif node.alternate:
            return self.evaluate(node.alternate, env)
        return None
    def eval_BlockStatement(self, node, env):
        block_env = Environment(env)
        result = None
        for stmt in node.body:
            result = self.evaluate(stmt, block_env)
        return result
    def eval_ExpressionStatement(self, node, env):
        return self.evaluate(node.expression, env)
    def eval_BinaryOperation(self, node, env):
        left = self.evaluate(node.left, env)
        right = self.evaluate(node.right, env)
        op = node.operator
        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/': return left / right
        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '<': return left < right
        if op == '<=': return left <= right
        if op == '>': return left > right
        if op == '>=': return left >= right
        raise ValueError(f"Unknown binary operator: {op}")
    def eval_UnaryOperation(self, node, env):
        val = self.evaluate(node.expression, env)
        if node.operator == '-': return -val
        if node.operator == '!': return not val
        raise ValueError(f"Unknown unary operator: {node.operator}")
    def eval_ArrowFunction(self, node, env):
        def fn(*args):
            fn_env = Environment(env)
            for i, param in enumerate(node.parameters):
                val = args[i] if i < len(args) else None
                fn_env.define(param.name, val)
            if hasattr(node.body, 'body'):
                result = None
                for stmt in node.body.body:
                    result = self.evaluate(stmt, fn_env)
                return result
            else:
                return self.evaluate(node.body, fn_env)
        return fn
    def eval_FunctionCall(self, node, env):
        callee = self.evaluate(node.callee, env)
        args = [self.evaluate(arg, env) for arg in node.arguments]
        if callable(callee):
            return callee(*args)
        raise TypeError(f"'{callee}' is not callable")
    def eval_ClassDeclaration(self, node, env):
        class_def = {'name': node.name.name, 'properties': {}, 'methods': {}}
        for prop in node.properties:
            class_def['properties'][prop.name.name] = None
        for method in node.methods:
            fn = self.eval_ArrowFunction(
                ArrowFunction(method.parameters, method.body, method.return_type), env)
            class_def['methods'][method.name.name] = fn
        def class_ctor(*args):
            instance = {'__class__': node.name.name, '__data__': {}}
            for prop in class_def['properties']:
                instance['__data__'][prop] = None
            for method_name, fn in class_def['methods'].items():
                instance[method_name] = fn
            if node.constructor:
                ctor_fn = self.eval_ArrowFunction(
                    ArrowFunction(node.constructor.parameters, node.constructor.body), env)
                ctor_fn(instance, *args)
            return instance
        env.define(node.name.name, class_ctor)
        return class_ctor
    def eval_RouteDefinition(self, node, env):
        # For demo: register as a function in env
        def route_handler(*args):
            route_env = Environment(env)
            return self.evaluate(node.body, route_env)
        env.define(f"route_{node.method}_{node.path}", route_handler)
        return route_handler
    def eval_ReturnStatement(self, node, env):
        return self.evaluate(node.argument, env) if node.argument else None
    def eval_MemberExpression(self, node, env):
        obj = self.evaluate(node.object, env)
        return obj[node.property] if isinstance(obj, dict) else getattr(obj, node.property)
