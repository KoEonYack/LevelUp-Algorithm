"""
    @ Baek 1850 최대공약수
    @ Prob. https://www.acmicpc.net/problem/1850
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""
from math import gcd

A, B = map(int, input().split())
res = gcd(A, B)
print("1" * res)


"""
3 4
>
1
---------

500000000000000000 500000000000000002
>
11


111 111111
>
111
"""