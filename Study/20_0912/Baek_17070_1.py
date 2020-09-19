"""
    @ Baek 17070 파이프 옮기기
    @ Prob. https://www.acmicpc.net/problem/17070
      Ref.  https://jaimemin.tistory.com/1245
    @ Algo: BFS + Backtracking
    @ Start day: 20. 09. 10.
    @ End day: 20. 09. 10.
"""

# .         가로      세로     대각
p_dirs = [[0, 1], [1, 0], [1, 1]]
ans = 0


def solution(y, x, p_type):
    global ans

    if y == N - 1 and x == N - 1:
        ans += 1;
        return

    for i, dirs in enumerate(p_dirs):
        next_y = y + dirs[0];
        next_x = x + dirs[1]

        if i == 0 and p_type == 1 or i == 1 and p_type == 0:
            continue

        if next_y >= N or next_x >= N or MAP[next_y][next_x] == 1:
            continue

        if i == 2 and (MAP[y][x + 1] == 1 or MAP[y + 1][x] == 1):
            continue

        solution(next_y, next_x, i)

    return ans


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

print(solution(0, 1, 0))

"""
3
0 0 0
0 0 0
0 0 0
>
1
-------
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
>
3
"""