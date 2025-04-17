# ⚙️ # CoreFlux Manifest

**CoreFlux** is an experimental full-stack programming language that unifies modern backend development, frontend components, and AI capabilities into a single, coherent syntax.

---

## 🎯 Why CoreFlux?

Modern development stacks are fragmented:
- Frontend: JavaScript, TypeScript, React
- Backend: Python, Java, Go
- AI: Python libraries, OpenAI SDKs

**CoreFlux** aims to replace this complexity with a **single language model** that:
- Natively supports API routes and UI components
- Embeds AI logic at the language level (not via external libraries)
- Works uniformly across the full stack

---

## 🧠 Philosophy

- **"One language to rule every layer"**
- Syntax: readable, composable, extensible
- Typing: lightweight, with optional static typing
- AI: integrated at the core, not as an add-on

---

## 🔧 Version 0.0.1 Features

- `print()` command
- `class` keyword for defining objects
- `fn` for methods
- `route GET /path => { ... }` — native REST routing
- AI Command: `ai.prompt("...")` *(coming in v0.0.2)*

---

## 🧪 Example

```cf
print("Hello world!")

class User(name: string) {
  fn greet() {
    return "Hi, " + self.name
  }
}

route GET /hello => {
  return User("Tony").greet()
}
