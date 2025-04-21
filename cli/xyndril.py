import sys
import os
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parser.parser import parse
from interpreter.runtime import execute

def run_file(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' does not exist.", file=sys.stderr)
        sys.exit(1)
    with open(filepath, "r") as file:
        code = file.read()
    tree = parse(code)
    execute(tree)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Xyndril CLI Launcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run a .nx file")
    run_parser.add_argument("file", type=str, help="Path to .nx source file")

    args = parser.parse_args()

    if args.command == "run":
        run_file(args.file)
