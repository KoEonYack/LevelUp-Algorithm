"""
    @ Baek 3034 앵그리 창영
    @ Prob. https://www.acmicpc.net/problem/3034
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 14
    @ End day: 20. 01. 14
"""


N, W, H = map(int, input().split())
Value = (W ** 2 + H ** 2) ** 0.5
for i in range(N):
    lenght = int(input())
    if Value >= lenght:
        print("DA")
    else:
        print("NE")

"""
5 3 4
3
4
5
6
7
>
DA
DA
DA
NE
NE
"""