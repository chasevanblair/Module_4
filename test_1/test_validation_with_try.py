"""

Program: average_scores.py

Author: Chase Van Blair

Last date modified: 6/7/2020


The purpose of this program is to accept test_1 input
and average it for each student

"""
import unittest

from input_validation.validation_with_try import average


class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)


if __name__ == "__main__":
    unittest.main()
