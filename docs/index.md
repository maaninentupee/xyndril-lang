# Xyndril Manifest (Technical Vision)

## ✨ What is Xyndril?

Xyndril is an experimental full-stack programming language designed to unify frontend, backend, and AI logic into a seamless development experience.

Unlike traditional stacks where developers must switch between multiple languages and tools (JavaScript, Python, OpenAI SDKs), Xyndril proposes a polyglot-compatible architecture: it is designed to work alongside other languages and tools, eliminating friction between layers while enabling optional unification through a shared syntax.

## 🔠 Philosophy
"One language to rule every layer — when you want it to"

- Readable and extensible syntax
- Lightweight typing with optional static types
- AI features embedded into the language core
- Native support for API routing and UI components
- Interop-first mindset: Xyndril can both stand alone or integrate with your existing stack

## 💡 Key Differentiators

| Feature              | Xyndril                              | Other Languages              |
|----------------------|--------------------------------------|------------------------------|
| Full-stack support   | ✅ Unified syntax, optional adoption  | ❌ Separated frontend/backend |
| AI integration       | ✅ Native syntax-level support        | ❌ External libs required     |
| REST routes          | ✅ Built-in routing                   | ❌ Defined in frameworks      |
| UI components        | ✅ (Planned) as native syntax         | ❌ Framework-dependent        |
| Interop support      | ✅ Designed for multi-language use    | ⚠️ Often secondary concern    |

## 🚀 Version 0.0.1 Features
- print() command
- class keyword for defining objects
- fn for methods
- route GET /path => { ... } — native REST routing
- let statements
- Arrow functions: let add = (a, b) => a + b
- Conditional logic with if/else
- ✨ AI Command: ai.prompt("...") (planned v0.0.2)

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

## 🚧 Runtime Architecture (Planned)
**Memory Management:**
- Static analysis of variables at compile time
- Stack allocation for primitives
- Heap with generational GC for complex types
- Region-based memory zones for task-specific speed

**Garbage Collection Strategy:**
- Generational GC
- Concurrent execution
- Incremental marking
- Region-based optimization

**State Synchronization:**
- Realtime sync between client and server
- Reactive dataflow model planned

## 🌍 Vision
Xyndril is not just a new syntax. It is an attempt to create a cohesive, AI-native programming world where API logic, UI elements, and AI behavior can all be expressed in one language — without excluding others.

One language. Unified syntax. Interoperable by design.

Xyndril empowers developers to choose how deeply they adopt it: as a single-language full-stack platform, a language for AI agent workflows, or a flexible interop layer alongside existing systems.

## 📚 Technical Spec Roadmap
| Design Files (Claude)       | Refactored Code (GPT)    |
|----------------------------|--------------------------|
| design/ast.cld.py          | → src/ast.py             |
| design/interpreter.cld.py  | → src/interpreter.py     |
| design/parser_spec.md      | → parser/xyndril.g4      |
| (REPL Design)              | → src/repl.py            |

Design files are used as a planning layer, and refactoring is done by GPT for final integration into the compiler.

## 🔍 See Also
- [GitHub Repository](https://github.com/maaninentupee/xyndril-kit)
- 📖 See the full project overview in the [README on GitHub](https://github.com/maaninentupee/zyndril-lang#readme)
