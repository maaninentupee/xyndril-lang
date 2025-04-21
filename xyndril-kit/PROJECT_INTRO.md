

<!--
📢 This file is the first entry point for any GPT agent or human developer.
Do not skip this file during onboarding or development.
-->

# 🧠 PROJECT_INTRO.md

This project defines the **Xyndril Programming Language** – a modern experimental full-stack, AI-native language. It unifies backend logic, frontend UI, and AI capabilities under one cohesive syntax and runtime.

## 🔍 Project Purpose

Xyndril aims to simplify full-stack development by introducing:

- A **unified syntax** for both frontend and backend
- **Built-in AI operations** like `ai.prompt()` and `ai.generate()`
- Support for **REST routes** like `route GET /api => { ... }`
- A **REPL and CLI** for rapid prototyping
- **GPT agent collaboration** for language evolution and documentation

## 📦 Project Structure

xyndril-kit/ ├── cli/ → CLI launcher (xyndril.py) ├── examples/ → Example .nx source files ├── parser/ → Tokenizer and parser modules ├── interpreter/ → AST interpreter and runtime logic ├── src/ → Refactored production modules ├── docs/ → MkDocs documentation site │ └── CNAME → www.xyndril.dev ├── PROJECT_INTRO.md → This file (context for agents & devs) ├── xyndril-manifest.md → Language philosophy and syntax ├── agent-guidelines.md → GPT agent rules & automation ├── CHANGELOG.md → Version history ├── tasks.template.json → Task system format (example) └── .gitignore → Git exclusions

markdown
Kopioi
Muokkaa

## 🤖 For GPT Agents

Before starting any task, **always read this file first** to understand:

1. The purpose of Xyndril
2. Where key files are located
3. The agent’s operational boundaries (defined in `agent-guidelines.md`)

### Required Reading

- `/docs/xyndril-manifest.md` → official language spec
- `/xyndril-kit/agent-guidelines.md` → automation rules
- `/xyndril-kit/tasks.json` → current task queue (if active)

## 🌐 Live Documentation

The official Xyndril docs are published at:  
🔗 [https://www.xyndril.dev](https://www.xyndril.dev)

## 📬 Contact

For collaboration or issues, contact:  
📧 `fusion@xyndril.dev`

