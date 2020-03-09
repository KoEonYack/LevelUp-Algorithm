"""
    @ Baek 2455 지능형 기차
    @ Prob. https://www.acmicpc.net/problem/2455
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

curr_M = 0
max_V = -1
for _ in range(4):
    out_V, in_V = map(int, input().split())
    curr_M += (in_V - out_V)
    if curr_M > max_V:
        max_V = curr_M

print(max_V)


"""
0 32
3 13
28 25
39 0
>
42
"""