# 🚀 Xyndril

Xyndril is an experimental full-stack programming language designed to unify modern backend, frontend components, and artificial intelligence into a single language core.

---

## 🔧 What's Included in This Version (v0.0.1)

- `print()` command
- Class (`class`) definitions
- REST API route definitions (`route GET`)
- Example file: `examples/hello.nx`
- Simple tokenizer, parser, and runtime (in Python)

---

## 🛠️ Running Xyndril

Make sure you have Python 3.9 or newer installed.

Run the program from the command line:

```bash
python cli/xyndril.py examples/hello.nx
```

🧭 Roadmap (v0.0.2+)
🔜 ai.prompt(), ai.generate() – AI commands
🔜 import – File imports
🔜 Modular structure
🔜 Optional static typing
🔜 REPL support

📁 Project Structure
xyndril-kit/
├── cli/                 # CLI launcher
│   └── xyndril.py
├── examples/            # Example programs (.nx)
│   └── hello.nx
├── parser/              # Tokenizer and parser
│   ├── tokenizer.py
│   └── parser.py
├── interpreter/         # Interpreter for AST evaluation
│   └── runtime.py
├── design/              # Claude design files
│   ├── ast.cld.py
│   ├── interpreter.cld.py
│   └── parser_spec.md
└── README.md

💡 Why Xyndril?
Current software development is fragmented across different languages:

👨‍💻 Backend (Python, Go...)
🌐 Frontend components (JS, React...)
🤖 Artificial Intelligence (OpenAI, langchain...)

Xyndril brings everything together in one language.

One language. One project. All layers.

---

## 🧠 Philosophy
"One language to rule every layer"

- Syntax: readable, extensible
- Type system: lightweight, optional
- AI: built-in feature, not just a library

---

## 🧪 Example Code
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
```

---

## 🧭 Roadmap
- ai.prompt(), ai.generate() – AI commands
- import – File imports
- Modular structure
- Optional static typing
- REPL support

---

## 📁 Folder Structure
```
xyndril-kit/
├── cli/                 # CLI launcher
│   └── xyndril.py
├── examples/            # Example programs (.nx)
│   └── hello.nx
├── parser/              # Tokenizer and parser
│   ├── tokenizer.py
│   └── parser.py
├── interpreter/         # Interpreter for AST evaluation
│   └── runtime.py
├── design/              # Claude design files
│   ├── ast.cld.py
│   ├── interpreter.cld.py
│   └── parser_spec.md
└── README.md
```

Design files in the `design/` folder include:
- AST specification: ast.cld.py
- Interpreter structure: interpreter.cld.py
- Parser description: parser_spec.md

These files are refactored by GPT into production code:
- src/ast.py
- src/interpreter.py
- parser/xyndril.g4
- src/repl.py (REPL support)

---

## 💡 Get Involved
Ready to try Xyndril or contribute?

📩 Contact: fusion@xyndril.dev
