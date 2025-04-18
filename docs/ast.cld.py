"""
Xyndril Abstract Syntax Tree (AST) Design

This module defines the Abstract Syntax Tree structure for the Xyndril language.
Each node type represents a different syntactic element in the language.
"""

class Node:
    """Base class for all AST nodes"""
    pass

# --- Expressions ---

class Expression(Node):
    """Base class for all expressions"""
    pass

class Literal(Expression):
    """Represents literal values (numbers, strings, booleans, etc.)"""
    def __init__(self, value, type_name):
        self.value = value
        self.type_name = type_name  # "String", "Number", "Boolean", etc.

class Identifier(Expression):
    """Represents variable or function names"""
    def __init__(self, name):
        self.name = name

class BinaryOperation(Expression):
    """Represents binary operations like addition, subtraction, etc."""
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator  # "+", "-", "*", "/", etc.
        self.right = right

class UnaryOperation(Expression):
    """Represents unary operations like negation"""
    def __init__(self, operator, expression):
        self.operator = operator  # "-", "!", etc.
        self.expression = expression

class FunctionCall(Expression):
    """Represents a function call"""
    def __init__(self, callee, arguments):
        self.callee = callee  # Identifier or MemberExpression
        self.arguments = arguments  # List of expressions

class MemberExpression(Expression):
    """Represents accessing a property of an object (e.g., obj.prop)"""
    def __init__(self, object_expr, property_name):
        self.object = object_expr
        self.property = property_name

class ArrowFunction(Expression):
    """Represents arrow function expressions"""
    def __init__(self, parameters, body, return_type=None):
        self.parameters = parameters  # List of Parameter objects
        self.body = body  # BlockStatement or Expression
        self.return_type = return_type  # Optional type annotation

# --- Statements ---

class Statement(Node):
    """Base class for all statements"""
    pass

class LetStatement(Statement):
    """Represents variable declarations with 'let'"""
    def __init__(self, identifier, type_annotation=None, initializer=None):
        self.identifier = identifier  # Identifier node
        self.type_annotation = type_annotation  # Optional type annotation
        self.initializer = initializer  # Optional initializer expression

class IfStatement(Statement):
    """Represents if statements"""
    def __init__(self, test, consequent, alternate=None):
        self.test = test  # Expression
        self.consequent = consequent  # BlockStatement
        self.alternate = alternate  # Optional BlockStatement (else branch)

class BlockStatement(Statement):
    """Represents a block of statements enclosed in curly braces"""
    def __init__(self, body):
        self.body = body  # List of statements

class ReturnStatement(Statement):
    """Represents return statements"""
    def __init__(self, argument=None):
        self.argument = argument  # Optional expression to return

class ExpressionStatement(Statement):
    """Represents an expression used as a statement"""
    def __init__(self, expression):
        self.expression = expression

# --- Classes ---

class ClassDeclaration(Statement):
    """Represents class declarations"""
    def __init__(self, name, properties, methods, constructor=None):
        self.name = name  # Identifier
        self.properties = properties  # List of PropertyDefinition objects
        self.methods = methods  # List of MethodDefinition objects
        self.constructor = constructor  # Optional constructor method

class PropertyDefinition(Node):
    """Represents class property definitions"""
    def __init__(self, name, type_annotation=None):
        self.name = name  # Identifier
        self.type_annotation = type_annotation  # Optional type annotation

class MethodDefinition(Node):
    """Represents class method definitions"""
    def __init__(self, name, parameters, body, return_type=None):
        self.name = name  # Identifier
        self.parameters = parameters  # List of Parameter objects
        self.body = body  # BlockStatement
        self.return_type = return_type  # Optional type annotation

class Parameter(Node):
    """Represents function parameters"""
    def __init__(self, name, type_annotation=None, default_value=None):
        self.name = name  # Identifier
        self.type_annotation = type_annotation  # Optional type annotation
        self.default_value = default_value  # Optional default value

# --- Routes ---

class RouteDefinition(Statement):
    """Represents REST API route definitions"""
    def __init__(self, method, path, parameters, body):
        self.method = method  # "GET", "POST", "PUT", "DELETE", etc.
        self.path = path  # String path pattern (e.g., "/users/:id")
        self.parameters = parameters  # List of Parameter objects
        self.body = body  # BlockStatement

# --- Programs ---

class Program(Node):
    """Represents a complete Xyndril program"""
    def __init__(self, body):
        self.body = body  # List of statements
