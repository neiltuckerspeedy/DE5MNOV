import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.calc.getsum(),10, "the sum is wrong")