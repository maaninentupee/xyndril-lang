# run_editor_agent.py

"""
Xyndril-lang REPL (Read-Eval-Print Loop)

Provides an interactive command-line interface for evaluating Xyndril statements.
Integrates the parser (parser/parser.py) and interpreter (src/interpreter.py).
"""

import sys
from parser.parser import parse_statement
from src.interpreter import Interpreter

def run_repl():
    """Run the Xyndril REPL, reading input, parsing, evaluating, and printing results."""
    print("Xyndril-lang REPL (type 'exit' to quit)")
    interpreter = Interpreter()

    while True:
        try:
            # Read input from the user
            user_input = input("xyndril> ")
            if user_input.lower() == "exit":
                print("Exiting REPL...")
                break

            # Ensure the input ends with a semicolon
            if not user_input.endswith(";"):
                user_input += ";"

            # Parse the input into an AST
            ast = parse_statement(user_input)

            # Evaluate the AST using the interpreter
            result = interpreter.evaluate(ast)

            # Print the result
            print(result)

        except Exception as e:
            # Print any errors (syntax errors, evaluation errors, etc.)
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Check if the script is run in REPL mode or CLI mode
    if len(sys.argv) == 1:
        run_repl()
    else:
        print("CLI mode not yet implemented. Use REPL mode by running without arguments.")

