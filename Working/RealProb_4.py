'''
    Del Prob1
'''

import itertools

def check(lst):
    hour = lst[0] * 10 + lst[1]
    min = lst[2] * 10 + lst[3]

    if (hour <= 24 and hour >= 1) and (min >= 0 and min <= 60):
        return True
    else:
        return False

def solution(A, B, C, D):
    iterable_list = [A, B, C, D]
    permutationList = list(itertools.permutations(iterable_list, 4))

    for lst in permutationList:
        if check(lst) is True:
            print(str(lst[0]) + str(lst[1]) + ":" + str(lst[2]) + str(lst[3]) )

    return

solution(9, 1, 3, 4)

