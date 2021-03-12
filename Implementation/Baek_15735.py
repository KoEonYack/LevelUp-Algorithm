"""
    @ Baek 15735 삼각
    @ Prob. https://www.acmicpc.net/problem/15735
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 19.
    @ End day: 20. 04. 19.
"""


N = int(input())
res = 0

for i in range(1, N+1):
    res += (i+1)*i // 2
# print(res)

A = 1
while N - A >= 1:
    res += (N - A) * (N - A + 1) //2
    A += 2

print(res)

"""
10
>
315
"""
