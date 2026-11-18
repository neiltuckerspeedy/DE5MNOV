import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        testCal = Calculator(8,2)
        self.assertEqual(testCal.get_sum(),10, "The Sum is wrong")

    def test_minus(self):
        testCal = Calculator(8,2)
        self.assertEqual(testCal.get_minus(),6,"The minus is wrong")

    def test_multiply(self):
        testCal = Calculator(8,2)
        self.assertEqual(testCal.get_multiply(), 16, "The multiply is wrong")

    def test_division(self):
        testCal = Calculator(8,2)
        self.assertEqual(testCal.get_division(),4,"The division is wrong")

if __name__ == "__main__":
    unittest.main()