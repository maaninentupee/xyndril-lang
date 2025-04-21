# src/repl.py
# Xyndril REPL (Read-Eval-Print Loop)
import sys

class DummyParser:
    """
    Placeholder parser for Xyndril REPL. In a real implementation, this would parse Xyndril source code to an AST.
    Currently, it uses Python's eval for demonstration.
    """
    def parse(self, line):
        try:
            return eval(line)
        except Exception as e:
            raise SyntaxError(f"Parse error: {e}")

class DummyInterpreter:
    """
    Placeholder interpreter for Xyndril REPL. In a real implementation, this would evaluate AST nodes.
    Currently, it just returns the node for demonstration.
    """
    def evaluate(self, node):
        return node

def main():
    print("Xyndril REPL. Type Xyndril code or AST node creation code. Ctrl+C or Ctrl+D to exit.")
    interpreter = DummyInterpreter()
    parser = DummyParser()
    while True:
        try:
            line = input('> ')
            if not line.strip():
                continue
            node = parser.parse(line)
            result = interpreter.evaluate(node)
            print(result)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting REPL.")
            break
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
