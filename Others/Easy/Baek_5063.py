"""
    @ Baek 5063 TGN
    @ Prob. https://www.acmicpc.net/problem/5063
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""

N = int(input())
for i in range(N):
    r, e, c = map(int, input().split())
    if r > e - c:
        print("do not advertise")
    elif r == e - c:
        print("does not matter")
    elif r < e - c:
        print("advertise")

"""
3
0 100 70
100 130 30
-100 -70 40
>
advertise
does not matter
do not advertise
"""