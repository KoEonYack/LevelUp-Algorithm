"""
    @ Baek 2979 트럭 주차
    @ Prob. https://www.acmicpc.net/problem/2979
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

A, B, C = map(int, input().split())
costs = [0] * 101

for _ in range(3):
    S, E = map(int, input().split())
    for i in range(S, E):
        costs[i] += 1

res = 0
for num in costs:
    if num == 0: continue
    elif num == 1:
        res += A
    elif num == 2:
        res += B * 2
    elif num == 3:
        res += C * 3

print(res)


"""
5 3 1
1 6
3 5
2 8
>
33
"""