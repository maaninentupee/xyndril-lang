# CHANGELOG

## 2025-04-21
- Added argparse-based CLI with 'run' subcommand to cli/xyndril.py. Now supports running .nx files with `xyndril run <file.nx>`. Added error handling and English-only messages. (Task: Improve CLI launcher)
- Implemented minimal REPL logic in src/repl.py: prompt, dummy parser/interpreter, error handling, English-only messages. Fixed SonarLint warnings (unused parameter, unused variable). (Task: Define REPL behavior)
