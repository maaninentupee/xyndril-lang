// CoreFlux ANTLR4 grammar (coreflux.g4)
grammar CoreFlux;

program: statement* EOF;

statement
    : letStatement
    | ifStatement
    | classDeclaration
    | routeDefinition
    | expressionStatement
    ;

letStatement
    : 'let' identifier (':' typeName)? ('=' expression)? (',' identifier (':' typeName)? ('=' expression)?)* ';'
    ;

ifStatement
    : 'if' '(' expression ')' block ('else' (block | ifStatement))?
    ;

classDeclaration
    : 'class' identifier classBody
    ;

classBody
    : '{' classElement* '}'
    ;

classElement
    : propertyDeclaration
    | methodDeclaration
    | constructorDeclaration
    | routeDefinition
    ;

propertyDeclaration
    : identifier (':' typeName)? ';'
    ;

methodDeclaration
    : identifier '(' parameterList? ')' (ARROW typeName)? block
    ;

constructorDeclaration
    : 'constructor' '(' parameterList? ')' block
    ;

routeDefinition
    : 'route' httpMethod pathPattern block
    ;

httpMethod
    : 'GET' | 'POST' | 'PUT' | 'DELETE'
    ;

pathPattern
    : '/' (identifier | ':' identifier | '/' | DIGIT)*
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : identifier (':' typeName)?
    ;

block
    : '{' statement* '}'
    ;

expressionStatement
    : expression ';'
    ;

expression
    : assignmentExpression
    ;

assignmentExpression
    : arrowFunction
    | binaryExpression
    ;

arrowFunction
    : '(' parameterList? ')' ARROW (block | expression)
    ;

binaryExpression
    : unaryExpression (binaryOp unaryExpression)*
    ;

unaryExpression
    : primaryExpression
    ;

primaryExpression
    : literal
    | identifier
    | functionCall
    | '(' expression ')'
    ;

functionCall
    : identifier '(' argumentList? ')'
    ;

argumentList
    : expression (',' expression)*
    ;

literal
    : NUMBER
    | STRING
    | 'true'
    | 'false'
    | 'null'
    ;

identifier
    : IDENTIFIER
    ;

typeName
    : IDENTIFIER
    ;

binaryOp
    : '+' | '-' | '*' | '/' | '==' | '!=' | '<' | '<=' | '>' | '>=' | '&&' | '||'
    ;

ARROW: '=>' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
STRING: '"' (~['"'])* '"' | '\'' (~['\''])* '\'' ;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;
DIGIT: [0-9];
WS: [ \t\r\n]+ -> skip ;
