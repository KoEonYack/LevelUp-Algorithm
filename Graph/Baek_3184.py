"""
    @ Baek 3184. 양
    @ Prob. https://www.acmicpc.net/problem/3184
     Ref. https://sejinik.tistory.com/59
    @ Algo: DFS
    @ Start day: 19. 12. 26.
    @ End day: 19. 12. 26.
"""

from collections import deque

def BFS():
    global wolf
    global sheep

    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] != '#' and ch[ny][nx] == 0:
                    if MAP[ny][nx] == '.':
                        q.append((ny, nx))
                        ch[ny][nx] = 1
                    elif MAP[ny][nx] == 'v':
                        q.append((ny, nx))
                        ch[ny][nx] = 1
                        wolf += 1
                    elif MAP[ny][nx] == 'o':
                        q.append((ny, nx))
                        ch[ny][nx] = 1
                        sheep += 1

    if wolf >= sheep: return (1, wolf)
    else: return (2, sheep)


# N: 세로 M: 가로
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
ch = [[0] * M for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()

total_wolf = 0; total_sheep = 0
wolf = 0
sheep = 0

for i in range(N):
    for j in range(M):
        if ch[i][j] == 0 and MAP[i][j] != '#':
            q.append((i, j))
            ch[i][j] = 1

            wolf = 0
            sheep = 0

            if MAP[i][j] == 'v':
                wolf += 1
            elif MAP[i][j] == 'o':
                sheep += 1

            case, num = BFS()
            if case == 1:  # 울프 이김
                total_wolf += num
            elif case == 2:
                total_sheep += num


print(total_sheep, total_wolf)
"""
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
>
0 2
--------------------
8 8
.######.
#..o...#
#.####.#
#.#v.#.#
#.#.o#o#
#o.##..#
#.v..v.#
.######.
>
3 1
---------------------
9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
>
3 5

"""