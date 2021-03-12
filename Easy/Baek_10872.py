"""
    백준 10872 팩토리얼
    End Day : 2020. 1. 1
"""

import sys
sys.setrecursionlimit(10000000)


def fac(N):
    if N <= 1:
        return 1
    else:
        return N * fac(N-1)


inputN = int(input())
print(fac(inputN))


"""
10
>>>

3628800
"""