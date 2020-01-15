"""
    @ Baek 1712 손익분기점
    @ Prob. https://www.acmicpc.net/problem/1712
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""

A, B, C = map(int, input().split())
i = 1
if B >= C:
    print(-1)
else:
    print(int(A / (C-B) + 1))

"""
1000 70 170
>   
11
"""

