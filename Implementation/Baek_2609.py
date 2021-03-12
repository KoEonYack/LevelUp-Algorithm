"""
    @ Baek 2609 최대공약수와 최소공배수
    @ Prob. https://www.acmicpc.net/problem/2609
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 17.
    @ End day: 20. 02. 17.
"""

from math import gcd

N, M = map(int, input().split())

print(gcd(N, M))        # 최대 공약수
print(N*M // gcd(N, M)) # 최소공배수

"""
24 18
>
6
72
"""
