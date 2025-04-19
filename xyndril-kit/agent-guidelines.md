<!--
📢 This project uses a GPT-4.1 agent for automated development and documentation.
Do not modify this section unless you are updating the project’s core context.
-->

# 🧠 Project Context: Xyndril Programming Language

Xyndril is a modern experimental full-stack programming language developed from the earlier CoreFlux prototype. It is designed to unify backend logic, frontend components, and AI capabilities into a single cohesive syntax and runtime.

## 🌐 Project Goals

- ✅ **Unified full-stack language**: One language to rule backend, frontend, and AI layers.
- ✅ **AI-native syntax**: Includes `ai.prompt()` and `ai.generate()` built-in.
- ✅ **REST API routing**: `route GET /example => {}` built into the language.
- ✅ **Simple, readable syntax** with optional static typing.
- ✅ **REPL & CLI support** for fast experimentation.
- ✅ **GPT-assisted development** and documentation using `agent-guidelines.md`.

## 📂 Repository Structure

xyndril-kit/ ├── cli/ → CLI launcher (xyndril.py) ├── examples/ → Sample programs (.nx files) ├── parser/ → Parser and tokenizer logic ├── interpreter/ → Runtime interpreter for AST ├── src/ → Refactored production code ├── docs/ → Markdown documentation for GitHub Pages ├── docs/CNAME → Custom domain: www.xyndril.dev ├── xyndril-manifest.md → Official language philosophy & overview └── agent-guidelines.md → GPT-4.1 operating rules


## 🌍 Public Site

Xyndril documentation is published at:  
🔗 [www.xyndril.dev](http://www.xyndril.dev)

## 📩 Contact

📬 **fusion@xyndril.dev**
























# 🧠 Agent Guidelines for Xyndril Documentation (MkDocs)

This file provides persistent instructions for the GPT-4.1 agent working on this project. Do **not** delete, rename, or modify this file unless instructed.

## 📁 File Locations

- All documentation source files must reside under the `docs/` directory.
- Do not reference or include files from outside this folder (e.g., `../design`, `../parser`) in either `mkdocs.yml` or Markdown links.

## 📚 mkdocs.yml: Navigation Setup

Only reference files that are physically located in `docs/` in the `nav:` section of `mkdocs.yml`.

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
nav:
  - Parser Spec: ../design/parser_spec.md  # This will break MkDocs!

📝 Markdown Linking
Use relative links inside docs/ only, without ../.

✅ Example:
Read the [parser spec](parser_spec.md) or visit the [workspace setup](workspace-setup.md).

❌ Avoid:
[parser spec](../design/parser_spec.md)

🧷 Reserved Files (Do Not Rename or Delete)
ohjeet.txt — Internal developer notes.

agent-guidelines.md — This file.

xyndril-manifest.md — Part of the official language documentation.

🔍 Testing and Live Preview
To preview documentation locally:
mkdocs serve -a localhost:8001

If you get an “address already in use” error:
lsof -t -i :8001 | xargs kill -9

📄 Optional files not in nav
If a file exists in docs/ but isn’t listed in nav:, it can still be served if accessed directly via URL (e.g. parser_spec.md). You may optionally add it to nav: if needed.

❌ Forbidden Actions for Agent
Do not auto-delete files like instructions.txt, ohjeet.txt, parser_spec.md, or workspace-setup.md.

Do not guess intent based on filename. Always ask or refer to this document.

🧠 These instructions are critical for the Xyndril documentation to stay valid and user-friendly. Agent must always verify link paths, navigation, and folder structure before pushing changes to GitHub or modifying navigation.

📤 Deployment Instructions (for GPT-4.1 agent)
Follow this exact sequence to safely deploy Xyndril documentation to GitHub Pages at www.xyndril.dev:

✅ Ensure .venv is activated

bash
Kopioi
Muokkaa
source .venv/bin/activate
✅ Build and deploy the documentation

bash
Kopioi
Muokkaa
mkdocs gh-deploy
✅ Confirm that the domain is correctly configured

Ensure docs/CNAME contains:

Kopioi
Muokkaa
www.xyndril.dev
✅ Check that DNS settings in your domain registrar include the following:


Type	Name	Value
A	@	185.199.108.153
A	@	185.199.109.153
A	@	185.199.110.153
A	@	185.199.111.153
CNAME	www	maaninentupee.github.io
🧪 Test the site

Visit: https://www.xyndril.dev

⚠️ If a warning appears about README.md not found, update the link in docs/xyndril-manifest.md:

markdown
Kopioi
Muokkaa
[README on GitHub](https://github.com/maaninentupee/zyndril-lang/blob/main/README.md)
🧠 This section ensures the GPT-4.1 agent can repeat this process precisely and safely in the future.
Do not modify unless the deployment pipeline is officially changed.