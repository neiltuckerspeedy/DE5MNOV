import unittest
import pandas.testing as pdt
from datetime import datetime
from pipeline_test import *

class TestOperations(unittest.TestCase):

    def testduration_neg(self):
            row = {
                'Book checkout': datetime(2026, 11, 18),
                'Book Returned': datetime(2026, 11, 16)
            }

            result = duration(row)

            self.assertEqual(result, -2, "Should be -2")

    def testduration_pos(self):
         row = {
                'Book checkout': datetime(2026, 11, 18),
                'Book Returned': datetime(2026, 11, 30)
            }
         
         result = duration(row)
         
         self.assertEqual(result, 12, "Should be 12")

    def testduration_zero(self):
         row = {
                'Book checkout': datetime(2026, 11, 18),
                'Book Returned': datetime(2026, 11, 18)
            }
         
         result = duration(row)

         self.assertEqual(result, 0, "Should be 0")

    def testquotereplace(self):
         testquote = pd.Series(['" some text "'])
         result = quotereplace(testquote)
         expected = pd.Series(['some text'])
         pdt.assert_series_equal(result,expected)


if __name__ == "__main__":
    unittest.main()