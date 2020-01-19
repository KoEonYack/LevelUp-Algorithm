"""
    @ 7. 알리바바와 40인의 도둑(Bottom-up)
    @ Start day: 20. 01. 18
    @ End day: 20. 01. 18
"""


N = int(input())
arr = []
dy = [[0] * N for _ in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))

dy[0][0] = arr[0][0]
for i in range(1, N):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[i-1][0] + arr[i][0]

for i in range(1, N):
    for j in range(1, N):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]


print(dy[N-1][N-1])

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