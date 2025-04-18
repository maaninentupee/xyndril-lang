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