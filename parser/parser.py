"""
Extended Parser for Xyndril-lang

Parses expressions (arithmetic with +, -, *, /, and parentheses) using ANTLR grammar (xyndril.g4)
and builds an AST structure aligned with src/ast.py.
"""

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from .xyndrilLexer import xyndrilLexer
from .xyndrilParser import xyndrilParser
from src.ast import Literal, BinaryOperation, Variable, Assignment

class SyntaxErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}:{column} - {msg}")

def parse_statement(input_str):
    """
    Parse a statement (expression or assignment) and return an AST node.
    Example input: "x = 42" or "(42 + 10) * 2"
    """
    input_stream = InputStream(input_str)
    lexer = xyndrilLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(SyntaxErrorListener())
    stream = CommonTokenStream(lexer)
    parser = xyndrilParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(SyntaxErrorListener())
    tree = parser.statement()  # statement on oletussääntö
    # Jos statement on expressionStatement, kaiva expression
    if hasattr(tree, 'expressionStatement') and tree.expressionStatement():
        expr_ctx = tree.expressionStatement()
        return build_ast(expr_ctx)
    return build_ast(tree)

def build_ast(tree):
    """
    Build an AST from the parse tree.
    Tukee:
    - Aritmeettiset lausekkeet: NUMBER, +, -, *, /, sulut
    - Sijoitus: IDENTIFIER = expr (let tai suora)
    """
    rule = type(tree).__name__
    # Suora sijoituslause (assignmentStatement tai assignment)
    def safe_ctx(ctx):
        if isinstance(ctx, list):
            return ctx[0]
        return ctx

    def get_identifier_text(ctx):
        ident = safe_ctx(ctx.identifier())
        return ident.getText()

    if rule in ("AssignmentStatementContext", "AssignmentContext"):
        var_name = get_identifier_text(tree)
        value = build_ast(safe_ctx(tree.expression()))
        return Assignment(var_name, value)
    # let-lause
    if rule == "LetStatementContext":
        var_name = get_identifier_text(tree)
        value = build_ast(safe_ctx(tree.expression())) if tree.expression() else None
        return Assignment(var_name, value)
    # Numero
    if hasattr(tree, 'NUMBER') and tree.NUMBER():
        number_ctx = safe_ctx(tree.NUMBER())
        value = float(number_ctx.getText())
        return Literal(value)
    # Muuttuja
    if hasattr(tree, 'IDENTIFIER') and tree.IDENTIFIER():
        ident_ctx = safe_ctx(tree.IDENTIFIER())
        name = ident_ctx.getText()
        return Variable(name)
    # Jos kyseessä on ExpressionStatementContext, palauta sen expression
    ctx_type = type(tree).__name__
    if ctx_type == "ExpressionStatementContext" and hasattr(tree, 'expression'):
        expr_ctx = tree.expression()
        return build_ast(expr_ctx)
    # Binäärioperaatiot (rekursiivinen, yksinkertaistettu, laajenna tarvittaessa)
    if ctx_type == "BinaryExpressionContext" and hasattr(tree, 'children') and tree.children:
        ops = ['+', '-', '*', '/']
        children = tree.children
        if len(children) == 3:
            left = build_ast(children[0])
            op_token = getattr(children[1], 'getText', lambda: None)()
            right = build_ast(children[2])
            if op_token in ops:
                return BinaryOperation(op_token, left, right)
    # Fallback: käy kaikki lapset läpi ja palauta ensimmäinen ei-None build_ast-tulos
    if hasattr(tree, 'children') and tree.children:
        for child in tree.children:
            result = build_ast(child)
            if result is not None:
                return result
    return None

if __name__ == "__main__":
    try:
        result = parse_statement("x = (42 + 10) * 2")
        print("Parsed AST:", result)
    except Exception as e:
        print("Error:", e)
