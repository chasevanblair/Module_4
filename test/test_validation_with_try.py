"""

Program: average_scores.py

Author: Chase Van Blair

Last date modified: 6/7/2020


The purpose of this program is to accept test input
and average it for each student

"""

from input_validation.validation_with_try import average


def test_average_exception(self):
    with self.assertRaises(ValueError):
        average(-90, 89, 78)
