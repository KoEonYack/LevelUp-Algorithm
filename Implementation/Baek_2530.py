"""
    @ Baek 2530 인공지능 시계
    @ Prob. https://www.acmicpc.net/problem/2530
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

H, M, curr_S = map(int, input().split())
input_S = int(input())
curr_S += input_S

M += curr_S // 60
H += M // 60

print(H % 24, M % 60, curr_S % 60)

"""
14 30 00
200
>
14 33 20
"""