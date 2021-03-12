"""
    @ Baek 11201 A+B - 7
    @ Prob. https://www.acmicpc.net/problem/11201
      Ref.
      Ref Prob.
    @ Algo: 구현(입출력과 사칙연산)
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

import sys

N = int(sys.stdin.readline())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #" + str(i+1) + ": "+ str(A + B))



"""
5
1 1
2 3
3 4
9 8
5 2

>

Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7

"""