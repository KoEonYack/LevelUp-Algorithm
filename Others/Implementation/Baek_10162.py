"""
    @ Baek 10162 전자레인지
    @ Prob. https://www.acmicpc.net/problem/10162
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 31
    @ End day: 20. 01. 31
"""

# 10, 5, 10s
N = int(input())

if N % 10 != 0:
    print(-1)
else:
    five = N // 300
    N = N % 300
    one = N // 60
    N = N % 60
    print(five, one, N // 10)

"""
100
>
0 1 4
"""