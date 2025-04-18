# Workspace Setup

This page describes how to set up the Xyndril programming language development environment.

## Prerequisites
- Python 3.10+
- Git
- (Optional) VS Code or Windsurf Editor

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/maaninentupee/xyndril-kit.git
   cd xyndril-kit
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Documentation Site
To preview the documentation locally:
```sh
mkdocs serve
```
Site will be available at http://localhost:8000

## Notes
- Only files in the `docs/` folder are published to the documentation site.
- Do not edit or move files in `design/`, `parser/`, or `ohjeet.txt` unless instructed.
