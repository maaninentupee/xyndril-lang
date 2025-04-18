# Workspace Setup

This guide explains how to set up a development environment for the Xyndril project.

## 1. Clone the Repository

Clone the Xyndril repository from GitHub:
```bash
git clone https://github.com/maaninentupee/xyndril-lang.git
cd xyndril-kit
```

## 2. Create and Activate a Virtual Environment (Recommended)

It is recommended to use a virtual environment for Python dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Project Dependencies

Install MkDocs and the Material theme for documentation:
```bash
pip install mkdocs mkdocs-material
```

## 4. Folder Structure Overview

- `docs/` — Markdown documentation and examples
- `src/` — Source code for the Xyndril language/interpreter
- `parser/` — Grammar files and parser code
- `design/` — Language and parser design documents
- `examples/` — Example Xyndril programs

## 5. Running the Documentation Locally

Start the documentation server:
```bash
mkdocs serve
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

## 6. Coding Standards

- All code, comments, and documentation must be in English.
- Use clear, descriptive variable and function names.
- Keep code modular and well-documented.

## 7. Additional Tips

- If you use an IDE (like VSCode), open the `xyndril-kit` folder as your workspace.
- Use `.venv` to isolate dependencies.
- For any issues, check the README.md or contact the maintainer.

---

This setup ensures a clean, reproducible environment for both development and documentation of the Xyndril project.
