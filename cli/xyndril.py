import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parser.parser import parse
from interpreter.runtime import execute

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        code = file.read()
    tree = parse(code)
    execute(tree)

