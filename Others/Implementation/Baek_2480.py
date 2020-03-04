"""
    @ Baek 2480 주사위 세개
    @ Prob. https://www.acmicpc.net/problem/2480
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A * 1000)
elif A == B:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
elif A == C:
    print(1000 + A * 100)
else:
    print(100 * max(A, B, C))

"""
3 3 6
>
1300

"""