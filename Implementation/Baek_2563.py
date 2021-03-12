"""
    @ Baek 2563 색종이
    @ Prob. https://www.acmicpc.net/problem/2563
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

cord = []
for i in range(int(input())):
    X, Y = map(int, input().split())
    for i in range(X, X+10):
        for j in range(Y, Y+10):
            if [i, j] not in cord:
                cord.append([i, j])

print(len(cord))

"""
3
3 7
15 7
5 2
>
260
"""