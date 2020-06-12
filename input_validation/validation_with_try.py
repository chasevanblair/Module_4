"""

Program: average_scores.py

Author: Chase Van Blair

Last date modified: 6/7/2020


The purpose of this program is to accept test_1 input
and average it for each student

"""


def average(in_1, in_2, in_3):
    final = [in_1, in_2, in_3]
    score1 = int(final[0])
    score2 = int(final[1])
    score3 = int(final[2])

    if score1 < 0:
        raise ValueError
    elif score2 < 0:
        raise ValueError
    elif score3 < 0:
        raise ValueError

    nums = (score1 + score2 + score3) / 3
    return nums


