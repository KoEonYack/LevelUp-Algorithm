"""
    @ Baek 1629 곱셈
    @ Prob. https://www.acmicpc.net/problem/1629
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 25.
    @ End day: 20. 02. 25.
"""

A, B, C = map(int, input().split())

res = 1
for i in range(B):
    res = res * A
    res = res % C

print(res)

"""
10 11 12
>
4
"""
