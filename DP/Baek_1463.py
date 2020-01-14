"""
    @ 1463. 1로 만들기
    @ Prob. https://www.acmicpc.net/problem/1463
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 13.
    @ End day: 20. 01. 13.
"""

import sys

N = int(input())
MAX = 1000001
DP = [sys.maxsize] * MAX
DP[1] = 0

for i in range(N):
    DP[i+1] = min(DP[i+1], DP[i] + 1)
