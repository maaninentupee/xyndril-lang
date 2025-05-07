# Unit tests for the Xyndril parser will be implemented here.

"""
Unit tests for the Xyndril parser
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import unittest
from parser.parser import parse_statement, Literal, BinaryOperation, Variable, Assignment

class TestParser(unittest.TestCase):
    def test_number(self):
        """Test parsing a single number"""
        node = parse_statement("42;")
        self.assertIsInstance(node, Literal)
        self.assertEqual(node.value, 42.0)

    def test_addition(self):
        """Test parsing an addition expression"""
        node = parse_statement("10 + 20;")
        self.assertIsInstance(node, BinaryOperation)
        self.assertEqual(node.operator, "+")
        self.assertIsInstance(node.left, Literal)
        self.assertEqual(node.left.value, 10.0)
        self.assertIsInstance(node.right, Literal)
        self.assertEqual(node.right.value, 20.0)

    def test_subtraction(self):
        """Test parsing a subtraction expression"""
        node = parse_statement("30 - 15;")
        self.assertIsInstance(node, BinaryOperation)
        self.assertEqual(node.operator, "-")
        self.assertIsInstance(node.left, Literal)
        self.assertEqual(node.left.value, 30.0)
        self.assertIsInstance(node.right, Literal)
        self.assertEqual(node.right.value, 15.0)

    def test_multiplication(self):
        """Test parsing a multiplication expression"""
        node = parse_statement("5 * 2;")
        self.assertIsInstance(node, BinaryOperation)
        self.assertEqual(node.operator, "*")
        self.assertIsInstance(node.left, Literal)
        self.assertEqual(node.left.value, 5.0)
        self.assertIsInstance(node.right, Literal)
        self.assertEqual(node.right.value, 2.0)

    def test_division(self):
        """Test parsing a division expression"""
        node = parse_statement("10 / 2;")
        self.assertIsInstance(node, BinaryOperation)
        self.assertEqual(node.operator, "/")
        self.assertIsInstance(node.left, Literal)
        self.assertEqual(node.left.value, 10.0)
        self.assertIsInstance(node.right, Literal)
        self.assertEqual(node.right.value, 2.0)

    def test_parentheses(self):
        """Test parsing an expression with parentheses"""
        node = parse_statement("(42 + 10) * 2;")
        self.assertIsInstance(node, BinaryOperation)
        self.assertEqual(node.operator, "*")
        self.assertIsInstance(node.right, Literal)
        self.assertEqual(node.right.value, 2.0)
        self.assertIsInstance(node.left, BinaryOperation)
        self.assertEqual(node.left.operator, "+")
        self.assertEqual(node.left.left.value, 42.0)
        self.assertEqual(node.left.right.value, 10.0)

    def test_variable(self):
        """Test parsing a variable reference"""
        node = parse_statement("x;")
        self.assertIsInstance(node, Variable)
        self.assertEqual(node.name, "x")

    def test_assignment(self):
        """Test parsing an assignment statement"""
        node = parse_statement("x = 42;")
        self.assertIsInstance(node, Assignment)
        self.assertEqual(node.name, "x")
        self.assertIsInstance(node.value, Literal)
        self.assertEqual(node.value.value, 42.0)

    def test_assignment_with_expression(self):
        """Test parsing an assignment with a complex expression"""
        node = parse_statement("x = (10 + 20) * 2;")
        self.assertIsInstance(node, Assignment)
        self.assertEqual(node.name, "x")
        self.assertIsInstance(node.value, BinaryOperation)
        self.assertEqual(node.value.operator, "*")
        self.assertIsInstance(node.value.left, BinaryOperation)
        self.assertEqual(node.value.left.operator, "+")
        self.assertEqual(node.value.left.left.value, 10.0)
        self.assertEqual(node.value.left.right.value, 20.0)
        self.assertEqual(node.value.right.value, 2.0)

if __name__ == "__main__":
    unittest.main()
