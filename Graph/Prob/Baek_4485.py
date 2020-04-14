"""
    @ Baek 4485. 녹색 옷 입은 애가 젤다지?
    @ Prob. https://www.acmicpc.net/problem/4485
     Ref.
    @ Algo: BFS
    @ Start day: 20. 04. 14.
    @ End day: 20. 04. 14.
"""

from collections import deque
import sys

def BFS():
    pass

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
q = deque()
k = 1

while True:
    N = int(input())
    if N == 0: break
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ch = [[sys.maxsize] * N for _ in range(N)]
    q.append((0, 0))
    ch[0][0] = MAP[0][0]

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy; nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if ch[ny][nx] > ch[y][x] + MAP[ny][nx]:
                    q.append((ny, nx))
                    ch[ny][nx] = ch[y][x] + MAP[ny][nx]

    print("Problem {}: {}".format(k, ch[-1][-1]))
    k += 1


"""
3
5 5 4
3 9 1
3 2 7



5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5

7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0
>
Problem 1: 20
Problem 2: 19
Problem 3: 36
"""