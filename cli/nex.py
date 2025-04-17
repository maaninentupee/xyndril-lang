from parser.parser import parse
from interpreter.runtime import execute

import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        code = file.read()
    tree = parse(code)
    execute(tree)
