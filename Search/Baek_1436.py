"""
    @ Baek 1436 영화감독 숌
    @ Prob. https://www.acmicpc.net/problem/1436
      Ref.
      Ref Prob.
    @ Algo: Brute-force
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

import sys
input = sys.stdin.readline

N = int(input())
i = 0
ans = 0
while True:
    i += 1
    if "666" in str(i) :
        ans += 1
    if ans == N:
        print(i)
        break

"""
2
>
1666

"""




