"""
    @ Baek 11653 소인수분해
    @ Prob. https://www.acmicpc.net/problem/11653
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 28
    @ End day: 20. 01. 28
"""

import sys

N = int(sys.stdin.readline())

while N >= 2:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            break
    N = N // i


"""
72
>
2
2
2
3
3
-----
3
>
3

"""