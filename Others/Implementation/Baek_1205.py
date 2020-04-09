"""
    @ Baek 1205 등수 구하기
    @ Prob. https://www.acmicpc.net/problem/1205
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 07.
    @ End day: 20. 04. 07.
"""

import sys

N, score, P = map(int, input().split())
# arr = list(map(int, input().split()))
arr = list(map(int, sys.stdin.readline().split()))

rank = 1

if P == 0:
    rank = -1
elif N == 0:
    rank = 1
elif N == P and arr[N-1] >= score:
    rank = -1
else:
    for i in range(N):
        if arr[i] > score:
            rank += 1
print(rank)

"""
3 90 10
100 90 80

>
2
------------------
10 1 10
10 9 8 7 6 5 4 3 2 1
>
-1
------------------

3 101 3
100 100 100
"""