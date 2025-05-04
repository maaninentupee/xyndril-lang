# Xyndril Parser Specification

## Overview
This document describes the design and logic of the Xyndril parser, implemented in `parser/parser.py` and defined by the ANTLR grammar (`xyndril.g4`).

## Polyglot & Interoperability
The Xyndril parser and AST are designed for extensibility and interoperability:
- The grammar is modular and can be extended to support new language constructs or foreign language embeddings.
- AST nodes support hybrid constructs, allowing foreign function calls and type representations.
- The parser is not monolithic; it is built to be embedded in polyglot runtimes and to parse/translate hybrid code that mixes Xyndril with other languages.
- Future extensions will include grammar rules for foreign language blocks, imports, and interop expressions (e.g., `py:math.sqrt(16)` or embedding JavaScript blocks).

This enables Xyndril to serve as a bridge language in multi-language projects, supporting seamless integration with Python, JavaScript, and other ecosystems.

## Parser Logic
The parser processes Xyndril source code as a sequence of statements and expressions, producing a structured AST for interpretation. Key features:

### Supported Statements and Constructs
- **Variable Declarations**: `let x = 42;`, `let y: Number;`, `let a = 1, b: Number = 2;`
- **Assignments**: `x = 42;`
- **If Statements**: `if (cond) { ... } else { ... }`
- **Return Statements**: `return;`, `return value;`
- **Class Declarations**: `class User { ... }`
- **Arrow Functions**: `(a, b) => a + b;`
- **REST Routes**: `route GET /users { ... }`
- **Expression Statements**: Any valid expression followed by `;`

### Expressions
- **Literals**: Numbers, strings, booleans, null
- **Identifiers**: Variable and function names
- **Binary Operations**: `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `<=`, `>`, `>=`, `&&`, `||`
- **Unary Operations**: `-a`, `!a`
- **Function Calls**: `foo(1, 2)`, `obj.method(arg)`
- **Member Access**: `user.name`, `array[0]`
- **Parentheses**: For grouping
- **Arrow Functions**: `(x, y) => x + y`

### Grammar Structure (ANTLR excerpt)
```
program: statement* EOF;

statement
    : letStatement
    | assignmentStatement
    | ifStatement
    | classDeclaration
    | routeDefinition
    | expressionStatement
    ;

letStatement: 'let' identifier (':' typeName)? ('=' expression)? (',' identifier (':' typeName)? ('=' expression)?)* ';';
assignmentStatement: identifier '=' expression;
ifStatement: 'if' '(' expression ')' block ('else' (block | ifStatement))?;
classDeclaration: 'class' identifier classBody;
routeDefinition: 'route' httpMethod pathPattern block;
expressionStatement: expression ';';
```

### AST Structure
The parser produces the following AST node types (see `src/ast.py`):
- `Program`
- `LetStatement`, `Assignment`, `IfStatement`, `ReturnStatement`, `ClassDeclaration`, `RouteDefinition`, `ExpressionStatement`
- `Literal`, `Identifier`, `BinaryOperation`, `UnaryOperation`, `FunctionCall`, `MemberExpression`, `ArrowFunction`
- `BlockStatement`, `PropertyDefinition`, `MethodDefinition`, `Parameter`

#### Example AST (for `let x = (1 + 2) * y;`):
```
LetStatement(
  identifier=Identifier('x'),
  initializer=BinaryOperation(
    operator='*',
    left=BinaryOperation('+', Literal(1), Literal(2)),
    right=Identifier('y')
  )
)
```

### Error Handling
The parser uses a custom `SyntaxErrorListener` for immediate, informative syntax errors (e.g., missing semicolons, invalid tokens, mismatched types).

## Example
Input:
```xyndril
let x = 42;
let y = (x + 10) * 2;
if (y > 100) {
  print("Large!");
} else {
  print("Small!");
}
```
AST (pseudocode):
- Program
  - LetStatement(x, Literal(42))
  - LetStatement(y, BinaryOperation('*', BinaryOperation('+', Identifier(x), Literal(10)), Literal(2)))
  - IfStatement(
      test=BinaryOperation('>', Identifier(y), Literal(100)),
      consequent=BlockStatement([...]),
      alternate=BlockStatement([...])
    )

## Future Extensions
- Loops (`while`, `for`)
- User-defined functions
- Pattern matching
- Modules and imports
- Enhanced error diagnostics

## Synchronization Checklist
- [ ] Grammar (`xyndril.g4`) matches this specification
- [ ] AST (`src/ast.py`) supports all constructs
- [ ] Interpreter supports all grammar constructs
- [ ] Tests cover all features and edge cases
- [ ] Documentation (this & language-spec.md) up to date

## Overview
This document specifies the design and logic of the Xyndril language parser, implemented in `parser/parser.py`. The parser uses an ANTLR-based grammar (`xyndril.g4`) to parse expressions and constructs an Abstract Syntax Tree (AST) aligned with `src/ast.py`.

## Parser Logic
The parser processes input expressions and builds an AST for evaluation by the interpreter (`src/interpreter.py`). It supports the following features:

### Supported Expressions
- **Number Literals**: Parses numeric values (e.g., `42`, `3.14`) into `NumberNode` objects.
- **Arithmetic Operations**:
  - Addition (`+`) and Subtraction (`-`): Supported as binary operations (e.g., `10 + 20`, `30 - 15`).
  - Multiplication (`*`) and Division (`/`): Supported as binary operations (e.g., `5 * 2`, `10 / 2`).
  - Operations are represented as `BinOpNode` objects in the AST.
- **Parentheses**: Supports nested expressions using parentheses (e.g., `(42 + 10) * 2`).

### AST Structure
The parser generates an AST using the following node types (defined in `src/ast.py`):
- `NumberNode`: Represents a numeric literal (e.g., `42` → `NumberNode(42.0)`).
- `BinOpNode`: Represents a binary operation with an operator (`+`, `-`, `*`, `/`), left operand, and right operand (e.g., `10 + 20` → `BinOpNode('+', NumberNode(10.0), NumberNode(20.0))`).

### Error Handling
- The parser uses a custom `SyntaxErrorListener` to raise exceptions on syntax errors, providing detailed error messages (e.g., "Syntax error at line 1:5 - missing ';'").

## Example
Input: `(42 + 10) * 2`
- The parser generates an AST:
  - Root: `BinOpNode('*', ..., ...)`
  - Left: `BinOpNode('+', NumberNode(42.0), NumberNode(10.0))`
  - Right: `NumberNode(2.0)`

## Future Extensions
- Support for variables and assignments (e.g., `x = 42`).
- Support for control structures (e.g., `if`, `while`).
- Enhanced error reporting with suggestions.


This document specifies the syntax for the Xyndril language and how the parser should recognize language constructs.

## 1. General Syntax

Xyndril uses a C-style syntax with curly braces, semicolons, and common operators. The language is designed to be familiar to developers with experience in JavaScript, TypeScript, and similar languages while incorporating unique features for full-stack development.

## 2. Lexical Structure

### 2.1 Comments

```
// Single-line comment

/* 
   Multi-line
   comment
*/
```

### 2.2 Literals

```
// Numbers
42         // Integer
3.14       // Float

// Strings
"hello"    // Double quotes
'world'    // Single quotes
`template ${expression}` // Template string with interpolation

// Booleans
true
false

// Null and undefined
null
undefined
```

### 2.3 Identifiers

Identifiers start with a letter or underscore, followed by any number of letters, digits, or underscores.

```
variableName
_privateVar
$element
```

## 3. Language Constructs

### 3.1 Variable Declarations with `let`

```
// Simple declaration
let name;

// With initialization
let age = 30;

// With type annotation
let email: String = "user@example.com";

// Multiple declarations
let x = 1, y = 2;
```

The parser should recognize:
- The `let` keyword
- An identifier
- Optional type annotation (`: TypeName`)
- Optional initializer (`= expression`)
- Multiple declarations separated by commas

### 3.2 If Statements

```
// Basic if
if (condition) {
  // statements
}

// If-else
if (condition) {
  // statements
} else {
  // statements
}

// If-else if-else
if (condition1) {
  // statements
} else if (condition2) {
  // statements
} else {
  // statements
}
```

The parser should recognize:
- The `if` keyword
- A parenthesized condition expression
- A block statement for the "then" branch
- Optional `else` keyword followed by a block statement or another if statement

### 3.3 Arrow Functions

```
// Simple arrow function
let add = (a, b) => a + b;

// Multi-line arrow function with block
let greet = (name) => {
  return `Hello, ${name}!`;
};

// With type annotations
let multiply = (x: Number, y: Number): Number => x * y;

// No parameters
let sayHello = () => "Hello!";
```

The parser should recognize:
- A parameter list (possibly empty) in parentheses
- Optional type annotations for parameters
- The arrow (`=>`) token
- An expression or block statement for the function body
- Optional return type annotation after the parameter list

### 3.4 Classes

```
class User {
  // Properties with type annotations
  name: String
  email: String
  age: Number
  
  // Constructor
  constructor(name, email, age) {
    this.name = name
    this.email = email
    this.age = age
  }
  
  // Method with return type
  greet() -> String {
    return `Hello, I'm ${this.name}!`
  }
  
  // Method with parameters
  updateEmail(newEmail: String) {
    this.email = newEmail
  }
}
```

The parser should recognize:
- The `class` keyword followed by an identifier
- A class body enclosed in curly braces
- Property declarations with optional type annotations
- Method declarations with an identifier, parameter list, optional return type, and block body
- A special `constructor` method

### 3.5 REST Routes

```
route GET /users {
  // Return all users
  return db.getUsers()
}

route POST /users {
  // Create a new user
  return db.createUser(request.body)
}

route GET /users/:id {
  // Get a specific user
  return db.getUser(params.id)
}

// Routes inside classes
class UserController {
  route GET /api/users {
    return this.getAllUsers()
  }
  
  getAllUsers() {
    // Implementation
  }
}
```

The parser should recognize:
- The `route` keyword
- HTTP method (GET, POST, PUT, DELETE, etc.)
- URL path with optional parameters (prefixed with `:`)
- Block body for route handler

## 4. Expressions

### 4.1 Binary Operators

Standard arithmetic, comparison, and logical operators:

```
// Arithmetic
a + b
a - b
a * b
a / b
a % b

// Comparison
a == b
a != b
a < b
a <= b
a > b
a >= b

// Logical
a && b
a || b
```

### 4.2 Unary Operators

```
-a      // Negation
!a      // Logical NOT
a++     // Increment
a--     // Decrement
```

### 4.3 Function Calls

```
print("Hello")
user.getName()
Math.max(1, 2, 3)
```

### 4.4 Member Access

```
user.name
array[0]
```

## 5. Statements

### 5.1 Return Statements

```
return;
return value;
```

### 5.2 Expression Statements

Any expression can be used as a statement:

```
foo();
a = b + c;
x++;
```

## 6. Program Structure

A Xyndril program consists of a sequence of statements and declarations at the top level:

```
// Imports (future feature)
import { Component } from 'library'

// Variable declarations
let config = {
  port: 3000
}

// Function declarations
let start = () => {
  // Implementation
}

// Class declarations
class App {
  // Implementation
}

// Route declarations
route GET / {
  return "Hello, World!"
}

// Main code
start()
```

## 7. Parsing Strategy

The parser should follow these steps:

1. Tokenize the input into a stream of tokens
2. Build a recursive descent parser that recognizes the language constructs
3. Construct an AST according to the structure defined in `ast.cld.py`
4. Handle error cases with informative error messages

The parser should be designed to be extensible for future language features.
