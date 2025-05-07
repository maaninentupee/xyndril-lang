# Unit tests for the Xyndril interpreter will be implemented here.

"""
Unit tests for the Xyndril interpreter
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from parser.parser import parse_statement
from src.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def test_number(self):
        """Test evaluating a single number"""
        node = parse_statement("42;")
        result = self.interpreter.evaluate(node)
        self.assertEqual(result, 42.0)

    def test_addition(self):
        """Test evaluating an addition expression"""
        node = parse_statement("10 + 20;")
        interpreter = Interpreter()
        result = interpreter.evaluate(node)
        self.assertEqual(result, 30.0)

    def test_subtraction(self):
        """Test evaluating a subtraction expression"""
        node = parse_statement("30 - 15;")
        interpreter = Interpreter()
        result = interpreter.evaluate(node)
        self.assertEqual(result, 15.0)

    def test_multiplication(self):
        """Test evaluating a multiplication expression"""
        node = parse_statement("5 * 2;")
        interpreter = Interpreter()
        result = interpreter.evaluate(node)
        self.assertEqual(result, 10.0)

    def test_division(self):
        """Test evaluating a division expression"""
        node = parse_statement("10 / 2;")
        interpreter = Interpreter()
        result = interpreter.evaluate(node)
        self.assertEqual(result, 5.0)

    def test_parentheses(self):
        """Test evaluating an expression with parentheses"""
        node = parse_statement("(42 + 10) * 2;")
        interpreter = Interpreter()
        result = interpreter.evaluate(node)
        self.assertEqual(result, 104.0)  # (42 + 10) * 2 = 52 * 2 = 104

    def test_assignment(self):
        """Test evaluating an assignment statement"""
        node = parse_statement("x = 42;")
        result = self.interpreter.evaluate(node)
        self.assertEqual(result, 42.0)
        self.assertEqual(self.interpreter.variables["x"], 42.0)

    def test_variable(self):
        """Test evaluating a variable reference after assignment"""
        self.interpreter.evaluate(parse_statement("x = 42;"))
        node = parse_statement("x;")
        result = self.interpreter.evaluate(node)
        self.assertEqual(result, 42.0)

    def test_assignment_with_expression(self):
        """Test evaluating an assignment with a complex expression"""
        node = parse_statement("x = (10 + 20) * 2;")
        result = self.interpreter.evaluate(node)
        self.assertEqual(result, 60.0)  # (10 + 20) * 2 = 60
        self.assertEqual(self.interpreter.variables["x"], 60.0)

if __name__ == "__main__":
    unittest.main()
