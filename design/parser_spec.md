# CoreFlux Parser Specification

This document specifies the syntax for the CoreFlux language and how the parser should recognize language constructs.

## 1. General Syntax

CoreFlux uses a C-style syntax with curly braces, semicolons, and common operators. The language is designed to be familiar to developers with experience in JavaScript, TypeScript, and similar languages while incorporating unique features for full-stack development.

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

A CoreFlux program consists of a sequence of statements and declarations at the top level:

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
