# Xyndril Language Specification

## Overview
Xyndril is a modern, extensible programming language designed for clarity and expressiveness. Unlike monolithic languages, Xyndril is architected for interoperability: it is intended to be used alongside other programming languages in the same environment (polyglot). The language and its runtime are modular and extensible, making it possible to:
- Call functions and use libraries from other languages (e.g. Python, JavaScript, etc.) within Xyndril code
- Expose Xyndril modules and logic to be called from other languages
- Integrate seamlessly in multi-language projects and runtimes (polyglot/interop)
- Extend the language and runtime with new features, types, or backends without breaking compatibility

This document describes Xyndril's syntax, semantics, and polyglot/interoperability goals, reflecting the current implementation and planned extensions.

## Polyglot & Interoperability
Xyndril is not a monolithic language. Its core design principles include:
- **Modularity**: Language features, runtime, and standard library are implemented as modules that can be extended or replaced.
- **Interoperability**: Xyndril supports calling and embedding code from other languages, and vice versa.
- **Extensibility**: The parser and AST are designed to support new language constructs and foreign language integration.
- **Polyglot Environments**: Xyndril can be embedded in, or extended to, polyglot runtimes (e.g., GraalVM, Python/C interop, etc.).

### Example Use Cases
- Calling a Python function from Xyndril:
  ```xyndril
  let result = py:math.sqrt(16);
  ```
- Embedding Xyndril logic in a Python application:
  ```python
  from xyndril import evaluate
  result = evaluate("let x = 42; x + 1;")
  ```
- Creating a hybrid module that combines Xyndril and JavaScript logic


## Syntax

### Statements
A Xyndril program consists of a sequence of statements, each terminated by a semicolon (`;`). Supported statement types:
- Variable declaration: `let x = 42;`, `let y: Number = (x + 10) * 2;`
- Assignment: `x = 42;`
- Expression statement: `(x + 10) * 2;`
- If statement:
  ```
  if (x > 0) {
    y = x;
  } else {
    y = -x;
  }
  ```
- Return statement: `return;`, `return value;`
- Class declaration, function/arrow function, and REST route definitions (see below)

### Expressions
- **Literals**: Numeric (`42`, `3.14`), string (`"hello"`), boolean (`true`, `false`), null (`null`).
- **Variables**: Identifiers (e.g., `x`, `myVar`).
- **Binary Operations**: `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `<=`, `>`, `>=`, `&&`, `||`
- **Unary Operations**: `-a`, `!a`
- **Parentheses**: For grouping, e.g., `(a + b) * c`
- **Function Calls**: `foo(1, 2)`, `obj.method(arg)`
- **Member Access**: `user.name`, `array[0]`
- **Arrow Functions**: `(a, b) => a + b`, `(x: Number): Number => x * x`

### Variable Declarations
- Syntax: `let IDENTIFIER (: TypeName)? (= expr)? [,...];`
- Examples:
  - `let x = 42;`
  - `let y: Number;`
  - `let a = 1, b: Number = 2;`

### Assignments
- Syntax: `IDENTIFIER = expr;`
- Example: `x = 42;`, `y = (10 + 20) * 2;`

### Functions
- Arrow function: `(a, b) => a + b;`
- With block: `(x) => { return x * x; };`
- With types: `(x: Number, y: Number): Number => x + y;`

### Classes
```
class User {
  name: String;
  email: String;
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }
  greet() -> String {
    return `Hello, I'm ${this.name}!`;
  }
}
```

### REST Routes
```
route GET /users {
  return db.getUsers();
}
```

## Semantics
- **Evaluation**:
  - Literals evaluate to their value.
  - Binary and unary operations are computed left-to-right.
  - Variables evaluate to their value in the current scope.
  - Assignments update variable values.
  - Function calls evaluate arguments and invoke the function.
  - Control flow: `if`, `while` (planned), etc.
- **Error Handling**:
  - Division by zero, undefined variables, invalid operations, and type errors raise runtime errors with informative messages.

## Example Program
```xyndril
let x = 42;
let y = (x + 10) * 2;
if (y > 100) {
  print("Large!");
} else {
  print("Small!");
}
```

## REPL (Read-Eval-Print Loop)
- **Overview**: Xyndril-lang provides an interactive REPL for evaluating statements.
- **Usage**: Run `python3 run_editor_agent.py` to start the REPL.
- **Features**:
  - Evaluates arithmetic expressions, variables, and assignments.
  - Displays results or error messages for each input.
  - Type `exit` to quit the REPL.
- **Example Session**:

xyndril> 42;
  42.0
xyndril> x = 10;
  10.0
xyndril> x;
  10.0
xyndril> (x + 20) * 2;
  60.0
xyndril> y;
  Error: Undefined variable: y
xyndril> exit
  Exiting REPL...


## Future Extensions
- Control structures: `while`, `for`, pattern matching
- User-defined functions and lambdas
- Type system: integers, strings, booleans, optionals
- Modules and imports
- Enhanced error reporting and diagnostics

## Synchronization Checklist
- [ ] Parser (`xyndril.g4`) matches this specification
- [ ] AST (`src/ast.py`) supports all constructs
- [ ] Interpreter executes all features
- [ ] Test suite covers new syntax and semantics
- [ ] Documentation (this file & parser_spec.md) updated for all changes

---
See [xyndril-manifest.md](xyndril-manifest.md) for the full manifest and language details.

See [xyndril-manifest.md](xyndril-manifest.md) for the full manifest and language details.

---

This file can be expanded with highlights or summaries of the language for quick reference.
