"""
    @ Baek 1934 최소공배수
    @ Prob. https://www.acmicpc.net/problem/1934
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

from math import gcd

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A < B: A, B = B, A
    print(A*B // gcd(A, B))


"""
3
1 45000
6 10
13 17
>
45000
30
221
"""