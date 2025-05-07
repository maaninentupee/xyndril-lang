# Generated from xyndril.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .xyndrilParser import xyndrilParser
else:
    from xyndrilParser import xyndrilParser

# This class defines a complete listener for a parse tree produced by xyndrilParser.
class xyndrilListener(ParseTreeListener):

    # Enter a parse tree produced by xyndrilParser#program.
    def enterProgram(self, ctx:xyndrilParser.ProgramContext):
        pass

    # Exit a parse tree produced by xyndrilParser#program.
    def exitProgram(self, ctx:xyndrilParser.ProgramContext):
        pass


    # Enter a parse tree produced by xyndrilParser#statement.
    def enterStatement(self, ctx:xyndrilParser.StatementContext):
        pass

    # Exit a parse tree produced by xyndrilParser#statement.
    def exitStatement(self, ctx:xyndrilParser.StatementContext):
        pass


    # Enter a parse tree produced by xyndrilParser#letStatement.
    def enterLetStatement(self, ctx:xyndrilParser.LetStatementContext):
        pass

    # Exit a parse tree produced by xyndrilParser#letStatement.
    def exitLetStatement(self, ctx:xyndrilParser.LetStatementContext):
        pass


    # Enter a parse tree produced by xyndrilParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:xyndrilParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by xyndrilParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:xyndrilParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by xyndrilParser#assignment.
    def enterAssignment(self, ctx:xyndrilParser.AssignmentContext):
        pass

    # Exit a parse tree produced by xyndrilParser#assignment.
    def exitAssignment(self, ctx:xyndrilParser.AssignmentContext):
        pass


    # Enter a parse tree produced by xyndrilParser#ifStatement.
    def enterIfStatement(self, ctx:xyndrilParser.IfStatementContext):
        pass

    # Exit a parse tree produced by xyndrilParser#ifStatement.
    def exitIfStatement(self, ctx:xyndrilParser.IfStatementContext):
        pass


    # Enter a parse tree produced by xyndrilParser#classDeclaration.
    def enterClassDeclaration(self, ctx:xyndrilParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by xyndrilParser#classDeclaration.
    def exitClassDeclaration(self, ctx:xyndrilParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by xyndrilParser#classBody.
    def enterClassBody(self, ctx:xyndrilParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by xyndrilParser#classBody.
    def exitClassBody(self, ctx:xyndrilParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by xyndrilParser#classElement.
    def enterClassElement(self, ctx:xyndrilParser.ClassElementContext):
        pass

    # Exit a parse tree produced by xyndrilParser#classElement.
    def exitClassElement(self, ctx:xyndrilParser.ClassElementContext):
        pass


    # Enter a parse tree produced by xyndrilParser#propertyDeclaration.
    def enterPropertyDeclaration(self, ctx:xyndrilParser.PropertyDeclarationContext):
        pass

    # Exit a parse tree produced by xyndrilParser#propertyDeclaration.
    def exitPropertyDeclaration(self, ctx:xyndrilParser.PropertyDeclarationContext):
        pass


    # Enter a parse tree produced by xyndrilParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:xyndrilParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by xyndrilParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:xyndrilParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by xyndrilParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:xyndrilParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by xyndrilParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:xyndrilParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by xyndrilParser#routeDefinition.
    def enterRouteDefinition(self, ctx:xyndrilParser.RouteDefinitionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#routeDefinition.
    def exitRouteDefinition(self, ctx:xyndrilParser.RouteDefinitionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#httpMethod.
    def enterHttpMethod(self, ctx:xyndrilParser.HttpMethodContext):
        pass

    # Exit a parse tree produced by xyndrilParser#httpMethod.
    def exitHttpMethod(self, ctx:xyndrilParser.HttpMethodContext):
        pass


    # Enter a parse tree produced by xyndrilParser#pathPattern.
    def enterPathPattern(self, ctx:xyndrilParser.PathPatternContext):
        pass

    # Exit a parse tree produced by xyndrilParser#pathPattern.
    def exitPathPattern(self, ctx:xyndrilParser.PathPatternContext):
        pass


    # Enter a parse tree produced by xyndrilParser#parameterList.
    def enterParameterList(self, ctx:xyndrilParser.ParameterListContext):
        pass

    # Exit a parse tree produced by xyndrilParser#parameterList.
    def exitParameterList(self, ctx:xyndrilParser.ParameterListContext):
        pass


    # Enter a parse tree produced by xyndrilParser#parameter.
    def enterParameter(self, ctx:xyndrilParser.ParameterContext):
        pass

    # Exit a parse tree produced by xyndrilParser#parameter.
    def exitParameter(self, ctx:xyndrilParser.ParameterContext):
        pass


    # Enter a parse tree produced by xyndrilParser#block.
    def enterBlock(self, ctx:xyndrilParser.BlockContext):
        pass

    # Exit a parse tree produced by xyndrilParser#block.
    def exitBlock(self, ctx:xyndrilParser.BlockContext):
        pass


    # Enter a parse tree produced by xyndrilParser#expressionStatement.
    def enterExpressionStatement(self, ctx:xyndrilParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by xyndrilParser#expressionStatement.
    def exitExpressionStatement(self, ctx:xyndrilParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by xyndrilParser#expression.
    def enterExpression(self, ctx:xyndrilParser.ExpressionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#expression.
    def exitExpression(self, ctx:xyndrilParser.ExpressionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:xyndrilParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:xyndrilParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#arrowFunction.
    def enterArrowFunction(self, ctx:xyndrilParser.ArrowFunctionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#arrowFunction.
    def exitArrowFunction(self, ctx:xyndrilParser.ArrowFunctionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#binaryExpression.
    def enterBinaryExpression(self, ctx:xyndrilParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#binaryExpression.
    def exitBinaryExpression(self, ctx:xyndrilParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#unaryExpression.
    def enterUnaryExpression(self, ctx:xyndrilParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#unaryExpression.
    def exitUnaryExpression(self, ctx:xyndrilParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:xyndrilParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by xyndrilParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:xyndrilParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by xyndrilParser#functionCall.
    def enterFunctionCall(self, ctx:xyndrilParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by xyndrilParser#functionCall.
    def exitFunctionCall(self, ctx:xyndrilParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by xyndrilParser#argumentList.
    def enterArgumentList(self, ctx:xyndrilParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by xyndrilParser#argumentList.
    def exitArgumentList(self, ctx:xyndrilParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by xyndrilParser#literal.
    def enterLiteral(self, ctx:xyndrilParser.LiteralContext):
        pass

    # Exit a parse tree produced by xyndrilParser#literal.
    def exitLiteral(self, ctx:xyndrilParser.LiteralContext):
        pass


    # Enter a parse tree produced by xyndrilParser#identifier.
    def enterIdentifier(self, ctx:xyndrilParser.IdentifierContext):
        pass

    # Exit a parse tree produced by xyndrilParser#identifier.
    def exitIdentifier(self, ctx:xyndrilParser.IdentifierContext):
        pass


    # Enter a parse tree produced by xyndrilParser#typeName.
    def enterTypeName(self, ctx:xyndrilParser.TypeNameContext):
        pass

    # Exit a parse tree produced by xyndrilParser#typeName.
    def exitTypeName(self, ctx:xyndrilParser.TypeNameContext):
        pass


    # Enter a parse tree produced by xyndrilParser#binaryOp.
    def enterBinaryOp(self, ctx:xyndrilParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by xyndrilParser#binaryOp.
    def exitBinaryOp(self, ctx:xyndrilParser.BinaryOpContext):
        pass



del xyndrilParser