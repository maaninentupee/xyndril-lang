# Xyndril Manifest (Technical Vision)

## ✨ What is Xyndril?

**Xyndril** is an experimental full-stack programming language designed to unify frontend, backend, and AI logic into a seamless development experience.

Unlike traditional stacks where developers must switch between multiple languages and tools (JavaScript, Python, OpenAI SDKs), Xyndril proposes a **single-language architecture** that eliminates friction between layers.

---

## 🔠 Philosophy

- **"One language to rule every layer"**
- Readable and extensible syntax
- Lightweight typing with optional static types
- AI features embedded into the language core
- Native support for API routing and UI components

---

## 💡 Key Differentiators

| Feature | Xyndril | Other Languages |
|--------|----------|-----------------|
| Full-stack support | ✅ One syntax for all layers | ❌ Separated frontend/backend |
| AI integration | ✅ Native in syntax | ❌ Requires external libs |
| REST routes | ✅ Part of the language | ❌ Defined in framework |
| UI components | ✅ (planned) native syntax | ❌ Framework-specific |

---

## 🚀 Version 0.0.1 Features

- `print()` command
- `class` keyword for defining objects
- `fn` for methods
- `route GET /path => { ... }` — native REST routing
- `let` statements
- Arrow functions: `let add = (a, b) => a + b`
- Conditional logic with `if/else`
- ✨ AI Command: `ai.prompt("...")` *(planned v0.0.2)*

---

## 🔢 Syntax Example

```cf
// Class definition
class User {
  name: String
  email: String
  age: Number

  constructor(name, email, age) {
    this.name = name
    this.email = email
    this.age = age
  }

  greet() -> String {
    return "Hello, I'm ${this.name}!"
  }

  route GET /user/:id {
    return this
  }
}

// Functional style
let double = (x: Number) -> Number => x * 2
let add = (a, b) => a + b

// Conditional logic
if (user.age >= 18) {
  console.log("Adult")
} else {
  console.log("Minor")
}

// Higher-order functions
let adults = users
  .filter(user => user.age >= 18)
  .map(user => user.name)
```

---

## 🚧 Runtime Architecture (Planned)

### Memory Management:
- Static analysis of variables at compile time
- Stack allocation for primitives
- Heap with generational GC for complex types
- Region-based memory zones for task-specific speed

### Garbage Collection Strategy:
- Generational GC
- Concurrent execution
- Incremental marking
- Region-based optimization

### State Synchronization:
- Realtime sync between client and server
- Reactive dataflow model planned

---

## 🌍 Vision

**Xyndril** is not just a new syntax. It is an attempt to create a cohesive, AI-native programming world where API logic, UI elements, and AI behavior are written in one language.

**One language. One stack. Total fusion.**

---

## 📚 Technical Spec Roadmap

| Design Files (Claude) | Refactored Code (GPT) |
|-----------------------|------------------------|
| `design/ast.cld.py` | → `src/ast.py` |
| `design/interpreter.cld.py` | → `src/interpreter.py` |
| `design/parser_spec.md` | → `parser/xyndril.g4` |
| *(REPL Design)* | → `src/repl.py` |

Design files are used as a planning layer, and refactoring is done by GPT for final integration into the compiler.

---

## 🔍 See Also
- [GitHub Repository](https://github.com/maaninentupee/xyndril-kit)
- `README.md` for introductory summary

