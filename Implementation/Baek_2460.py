"""
    @ Baek 2460 지능형 기차 2
    @ Prob. https://www.acmicpc.net/problem/2460
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 06.
    @ End day: 20. 03. 06.
"""

curr_M = 0
max_V = -1
for _ in range(10):
    out_V, in_V = map(int, input().split())
    curr_M += (in_V - out_V)
    if curr_M > max_V:
        max_V = curr_M

print(max_V)



"""
0 32
3 13
28 25
17 5
21 20
11 0
12 12
4 2
0 8
21 0
>
42
"""