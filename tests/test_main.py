import unittest
from app.main import add, mul


class TestMathOperations(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed(self):
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_mul_positive(self):
        self.assertEqual(mul(2, 3), 6)

    def test_mul_negative(self):
        self.assertEqual(mul(-2, -3), 6)

    def test_mul_mixed(self):
        self.assertEqual(mul(-2, 3), -6)

    def test_mul_zero(self):
        self.assertEqual(mul(5, 0), 0)
