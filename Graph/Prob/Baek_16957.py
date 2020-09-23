"""
    @ Baek 16957. 체스판 위의 공
    @ Prob. https://www.acmicpc.net/problem/16953
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

# N: 세로, M: 가로
N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
check = [[-1] * M for _ in range(N)]




"""
3 3
1 3 4
5 6 7
8 9 2
>
6 0 0
0 0 0
0 0 3
"""