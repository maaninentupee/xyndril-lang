

📋 Task Queue System (Autonomous Mode)
🧠 This project uses a structured autonomous task file:
📄 xyndril-kit/tasks.json

GPT agents must always:

Read tasks.json before performing any task

Locate the first item with "status": "todo"

Execute based on the title, description, and related_files

Mark progress ("in_progress" → "done"), if allowed

Skip or report "blocked" tasks

✅ JSON Task Structure
json
Kopioi
Muokkaa
{
  "id": "task-001",
  "title": "Implement basic REPL",
  "description": "Create REPL logic under src/repl.py",
  "status": "todo",
  "related_files": ["src/repl.py"]
}
status values: todo, in_progress, done, blocked

Agents must not modify unrelated fields or reorder tasks

Human developers may manually add or finish tasks if needed

🚫 Manual Editing Warning
Do not edit tasks.json manually unless:

You're debugging

You're adding a new task

You're confirming a completed task for documentation

📌 This file is critical for agent autonomy and must remain consistent.













<!--
📢 This project uses a GPT-4.1 agent for automated development and documentation.
Do not modify this section unless you are updating the project’s core context.
-->

# 🧠 Project Context: Xyndril Programming Language

👉 **IMPORTANT for GPT Agents:**  
Start with `PROJECT_INTRO.md` in `xyndril-kit/` as the primary onboarding file before doing anything else.

Xyndril is a modern experimental full-stack programming language developed from the earlier CoreFlux prototype. It is designed to unify backend logic, frontend components, and AI capabilities into a single cohesive syntax and runtime.

## 🌐 Project Goals

- ✅ **Unified full-stack language**: One language for backend, frontend, and AI layers
- ✅ **AI-native syntax**: Includes `ai.prompt()` and `ai.generate()` built-in
- ✅ **REST API routing**: `route GET /example => {}` support
- ✅ **Simple, readable syntax** with optional static typing
- ✅ **REPL & CLI support** for fast experimentation
- ✅ **GPT-assisted development** and documentation

## 📂 Repository Structure

xyndril-kit/ ├── cli/ → CLI launcher (xyndril.py) ├── examples/ → Sample programs (.nx files) ├── parser/ → Parser and tokenizer logic ├── interpreter/ → AST interpreter runtime ├── src/ → Refactored production code ├── docs/ → Markdown docs for GitHub Pages │ └── CNAME → www.xyndril.dev ├── PROJECT_INTRO.md → Agent onboarding and context ├── xyndril-manifest.md → Official language philosophy └── agent-guidelines.md → GPT-4.1 agent instructions

less
Kopioi
Muokkaa

## 🌍 Public Site

📘 Official docs: [www.xyndril.dev](https://www.xyndril.dev)  
📬 Contact: fusion@xyndril.dev

---

# 🧠 Agent Guidelines for Xyndril Documentation (MkDocs)

This section ensures the GPT-4.1 agent works safely and reliably.

## 📁 File Locations

- All documentation source files must reside under the `docs/` directory.
- Do **not** reference or include files from outside this folder (e.g., `../parser`) in either `mkdocs.yml` or Markdown links.

## 📚 mkdocs.yml Navigation Rules

✅ Correct:

```yaml
nav:
  - Home: index.md
  - Language Spec: language-spec.md
  - Parser Spec: parser_spec.md
  - Usage Guide: usage.md
  - Workspace Setup: workspace-setup.md
  - Xyndril Manifest: xyndril-manifest.md
❌ Incorrect:

yaml
Kopioi
Muokkaa
nav:
  - Parser Spec: ../design/parser_spec.md  # ❌ Will break MkDocs
📝 Markdown Linking
✅ Allowed:

md
Kopioi
Muokkaa
[parser spec](parser_spec.md)
❌ Forbidden:

md
Kopioi
Muokkaa
[parser spec](../design/parser_spec.md)
🔐 Reserved Files
agent-guidelines.md → This file

PROJECT_INTRO.md → Agent onboarding

xyndril-manifest.md → Official language spec

ohjeet.txt → Temporary internal notes (ignored)

raportti.md → Agent working memory (ignored)

🔍 Testing and Live Preview
To preview documentation locally:

bash
Kopioi
Muokkaa
mkdocs serve -a localhost:8001
If port 8001 is in use:

bash
Kopioi
Muokkaa
lsof -t -i :8001 | xargs kill -9
📤 Deployment Instructions (for GPT-4.1 agent)
Follow these exact steps to publish the documentation at www.xyndril.dev:

✅ 1. Activate virtual environment:

bash
Kopioi
Muokkaa
source .venv/bin/activate
✅ 2. Build and deploy the documentation:

bash
Kopioi
Muokkaa
mkdocs gh-deploy
✅ 3. Confirm docs/CNAME contains:

Kopioi
Muokkaa
www.xyndril.dev
✅ 4. Ensure DNS settings at your domain registrar:


Type	Name	Value
A	@	185.199.108.153
A	@	185.199.109.153
A	@	185.199.110.153
A	@	185.199.111.153
CNAME	www	maaninentupee.github.io
✅ 5. Verify site is live:
🔗 https://www.xyndril.dev

⚠️ If a README warning appears, update the link in xyndril-manifest.md:

md
Kopioi
Muokkaa
[README on GitHub](https://github.com/maaninentupee/zyndril-lang/blob/main/README.md)
📦 Versioning & Releases
Document all changes in CHANGELOG.md

Use semantic versioning (v0.0.1, v0.0.2, ...)

Reflect version bump in site (e.g., footer) if needed

🔁 REPL Support Planning
src/repl.py is reserved for REPL implementation

Do not overwrite or delete without confirmed REPL logic

When REPL is ready, update CLI and nav if needed

🧰 Quick Deployment Commands (for GPT-4.1 agent)
bash
Kopioi
Muokkaa
# ✏️ Add changelog entry
echo -e "\n## v0.0.X – Short description\n\n✅ Feature 1\n✅ Feature 2\n" >> CHANGELOG.md

# 📦 Commit and push
git add CHANGELOG.md
git commit -m "Add changelog entry for v0.0.X"
git push origin main

# 🌍 Deploy to GitHub Pages
source .venv/bin/activate
mkdocs gh-deploy
🔁 Repeat these steps for every documented version or published change.

📌 Don’t forget to bump the version number and summarize the changes.


## 📋 Task Queue System (Autonomous Mode)

🧠 This project uses a structured autonomous task file:  
📄 `xyndril-kit/tasks.json`

GPT agents must always:

- Read `tasks.json` before performing any task
- Locate the first item with `"status": "todo"`
- Execute based on the `title`, `description`, and `related_files`
- Update task progress (`"in_progress"` → `"done"`), if allowed
- Skip or report `"blocked"` tasks

---

### ✅ JSON Task Format

```json
{
  "id": "task-001",
  "title": "Implement basic REPL",
  "description": "Create REPL logic under src/repl.py",
  "status": "todo",
  "related_files": ["src/repl.py"]
}
Valid status values:
todo, in_progress, done, blocked

Agents must not modify unrelated fields or reorder tasks

Human developers may manually add or update tasks

🚫 Manual Editing Warning
Do not edit tasks.json manually unless:

You're debugging

You're adding a new task

You're confirming a completed task for documentation

📌 This file is critical for autonomous agent workflow and must remain consistent.
---

