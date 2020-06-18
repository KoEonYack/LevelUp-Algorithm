"""
    @ Baek 18883
    @ Prob. https://www.acmicpc.net/problem/17413
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

N, M = map(int, input().split())
c = 1
for i in range(N):
    for j in range(M):
        if j != M - 1:
            print(c, end=" ")
        else:
            print(c)
        c += 1


"""
3 4
>
1 2 3 4
5 6 7 8
9 10 11 12
"""