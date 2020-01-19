"""
    @ 8. 알리바바와 40인의 도둑(Top-Down)
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""


def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
            return dy[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
            return dy[x][y]
        else:
            dy[x][y] = arr[x][y] + min(DFS(x - 1, y), DFS(x, y-1))
            return dy[x][y]



N = int(input())
arr = []
dy = [[0] * N for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

print(DFS(N-1, N-1))


"""
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
>
25
"""