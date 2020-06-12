"""

Program: average_scores.py

Author: Chase Van Blair

Last date modified: 6/7/2020


The purpose of this program is to accept test_1 input
and average it for each student

"""
#from test_1.test_validation_with_try import test_average_exception


def average(in_1, in_2, in_3):
    #scores_input = input("enter the 3 test_1 scores to be averaged separated by comma: ")
    #final = scores_input.split(",")
    final = [in_1, in_2, in_3]
    score1 = int(final[0])
    score2 = int(final[1])
    score3 = int(final[2])

    nums = (score1 + score2 + score3) / 3
    return nums


#test_average_exception()

