"""
    @ Baek 1676 팩토리얼 0의 개수
    @ Prob. https://www.acmicpc.net/problem/1676
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26.
    @ End day: 20. 01. 26.
"""
from math import factorial

count = 0
n = factorial(int(input()))
while n % 10 == 0:
    n = n//10
    count += 1
print(count)

"""
10
>
2
"""