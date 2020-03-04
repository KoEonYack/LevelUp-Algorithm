"""
    @ Baek 2476 주사위 게임
    @ Prob. https://www.acmicpc.net/problem/2476
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

ans = []
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    if A == B == C:
        ans.append(10000 + A * 1000)
    elif A == B:
        ans.append(1000 + A * 100)
    elif B == C:
        ans.append(1000 + B * 100)
    elif A == C:
        ans.append(1000 + A * 100)
    else:
        ans.append(100 * max(A, B, C))

print(max(ans))

"""
3
3 3 6
2 2 2
6 2 5
>
12000
"""