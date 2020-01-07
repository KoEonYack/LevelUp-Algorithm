"""
    @ Baek 5532 방학 숙제
    @ Prob. https://www.acmicpc.net/problem/5532
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korea_day = math.ceil(A/C)
math_day = math.ceil(B/D)
print(L - max(korea_day, math_day))

"""
20
25
30
6
8
>
15
"""
