"""
    @ Baek 2869 달팽이는 올라가고 싶다
    @ Prob. https://www.acmicpc.net/problem/2869
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 14
    @ End day: 20. 01. 14
"""

import math

# 올라감, 내려감
A, B, V = map(int, input().split())

if V == A:
    print(1)
else:
    print(int(math.ceil((V-A)/(A-B)) + 1))

"""
2 1 5
>
4
"""