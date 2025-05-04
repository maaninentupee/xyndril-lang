# src/ast.py
# Xyndril AST (Abstract Syntax Tree) production implementation

class Node:
    """Base class for all AST nodes."""
    pass

# --- Expressions ---

class Expression(Node):
    pass

class Literal(Expression):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Literal({self.value})"

class Identifier(Expression):
    def __init__(self, name):
        self.name = name

class BinaryOperation(Expression):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right
    def __repr__(self):
        return f"BinaryOperation('{self.operator}', {self.left}, {self.right})"

class UnaryOperation(Expression):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

class FunctionCall(Expression):
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments

class MemberExpression(Expression):
    def __init__(self, object_expr, property_name):
        self.object = object_expr
        self.property = property_name

class ArrowFunction(Expression):
    def __init__(self, parameters, body, return_type=None):
        self.parameters = parameters
        self.body = body
        self.return_type = return_type

# --- Statements ---

class Statement(Node):
    pass

class LetStatement(Statement):
    def __init__(self, identifier, type_annotation=None, initializer=None):
        self.identifier = identifier
        self.type_annotation = type_annotation
        self.initializer = initializer

class IfStatement(Statement):
    def __init__(self, test, consequent, alternate=None):
        self.test = test
        self.consequent = consequent
        self.alternate = alternate

class BlockStatement(Statement):
    def __init__(self, body):
        self.body = body

class ReturnStatement(Statement):
    def __init__(self, argument=None):
        self.argument = argument

class ExpressionStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

# --- Classes ---

class ClassDeclaration(Statement):
    def __init__(self, name, properties, methods, constructor=None):
        self.name = name
        self.properties = properties
        self.methods = methods
        self.constructor = constructor

class PropertyDefinition(Node):
    def __init__(self, name, type_annotation=None):
        self.name = name
        self.type_annotation = type_annotation

class MethodDefinition(Node):
    def __init__(self, name, parameters, body, return_type=None):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.return_type = return_type

class Parameter(Node):
    def __init__(self, name, type_annotation=None, default_value=None):
        self.name = name
        self.type_annotation = type_annotation
        self.default_value = default_value

# --- Routes ---

class RouteDefinition(Statement):
    def __init__(self, method, path, parameters, body):
        self.method = method
        self.path = path
        self.parameters = parameters
        self.body = body

# --- Programs ---

class Program(Node):
    def __init__(self, body):
        self.body = body

class Variable(Expression):
    """Represents a variable reference in the AST"""
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Variable('{self.name}')"

class Assignment(Expression):
    """Represents an assignment in the AST (e.g., x = 42)"""
    def __init__(self, name, value):
        self.name = name  # Variable name (string)
        self.value = value  # Expression node (e.g., Literal)
    def __repr__(self):
        return f"Assignment('{self.name}', {self.value})"
