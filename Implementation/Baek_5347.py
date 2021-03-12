"""
    @ Baek 5347 LCM
    @ Prob. https://www.acmicpc.net/problem/5347
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

from math import gcd

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(A*B // gcd(A,B))


"""
3
15 21
33 22
9 10
>
105
66
90
"""