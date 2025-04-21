# Project Structure: Xyndril-lang

This document provides a detailed listing of the directories and files in the Xyndril-lang project (max depth: 3), with a brief description of each.

## Root Directory
- `.git/` — Git version control directory.
- `.gitignore` — Specifies files ignored by Git.
- `.venv/` — Python virtual environment.
- `README-agent.txt` — Agent-specific readme.
- `README.md` — Main project readme.
- `WORKSPACE_SETUP.md` — Workspace setup instructions.
- `cli/` — CLI entry point for Xyndril.
- `design/` — Design documents.
- `docs/` — Project documentation and specifications.
- `docs_sphinx/` — Sphinx documentation build and source.
- `examples/` — Example Xyndril source files.
- `interpreter/` — Interpreter runtime code.
- `ohjeet.txt` — Project instructions (in Finnish).
- `parser/` — Parser and tokenizer modules.
- `raportti.md` — Report file (in Finnish).
- `site/` — Static site output (possibly for docs).
- `src/` — Main source code (AST, interpreter, REPL).
- `tasks.json` — Task definitions/configuration.
- `tools/` — (Empty) Tools directory.
- `xyndril-kit/` — Project meta files and agent guidelines.
- `xyndril.code-workspace` — VS Code workspace file.

## Key Subdirectories and Files

### cli/
- `xyndril.py` — CLI entry point script.

### design/
- `xyndril-manifest.md` — Manifest and design notes.

### docs/
- `CNAME` — Custom domain for documentation site.
- `ast.cld.py` — AST class definitions (Python).
- `examples/` — Example files for documentation.
- `index.md` — Documentation index.
- `instructions.txt` — Additional instructions.
- `interpreter.cld.py` — Interpreter class definitions (Python).
- `language-spec.md` — Language specification.
- `parser_spec.md` — Parser specification.
- `usage.md` — Usage instructions.
- `workspace-setup.md` — Workspace setup for docs.
- `xyndril-manifest.md` — Manifest for docs.
- `xyndril.g4` — ANTLR grammar file.

### docs_sphinx/
- `Makefile` — Sphinx build script.
- `build/` — Sphinx build output.
- `source/` — Sphinx documentation sources.

### examples/
- `hello.nx` — Example Xyndril code.

### interpreter/
- `runtime.py` — Interpreter runtime support.

### parser/
- `parser.py` — Parser implementation (calls tokenizer, returns AST skeleton).
- `tokenizer.py` — Tokenizer implementation (tokenizes code into tokens).

### src/
- `ast.py` — AST node definitions.
- `interpreter.py` — Interpreter implementation (evaluates AST).
- `repl.py` — Read-Eval-Print Loop (REPL) for Xyndril.

### xyndril-kit/
- `CHANGELOG.md` — Project changelog.
- `PROJECT_INTRO.md` — Project introduction.
- `agent-guidelines.md` — Agent guidelines.
- `src/repl.py` — Placeholder for REPL (not yet implemented).
- `tasks.template.json` — Task template configuration.

### tools/
- (Empty)

---

Descriptions are based on actual file contents and structure. Placeholder or empty files are not listed unless they serve a clear structural purpose.
