# src/repl.py
# CoreFlux REPL (Read-Eval-Print Loop)
from src.ast import *
from src.interpreter import Interpreter

import sys

class DummyParser:
    # Placeholder parser: expects user to type Python AST node creation code
    def parse(self, line):
        # In oikea parseri, tämä muuntaisi CoreFlux-kieltä AST:ksi
        # Nyt vain eval Pythonilla testitarkoitukseen
        return eval(line)

def main():
    print("CoreFlux REPL. Type AST node creation code. Ctrl+C to exit.")
    interpreter = Interpreter()
    parser = DummyParser()
    env = None
    while True:
        try:
            line = input('> ')
            if not line.strip():
                continue
            node = parser.parse(line)
            result = interpreter.evaluate(node, env)
            print(result)
        except KeyboardInterrupt:
            print("\nExiting REPL.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
