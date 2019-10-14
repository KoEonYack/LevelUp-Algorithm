'''
    @ 47. 봉우리
    @ Idea.
    @ TestCase:
        input:  5
                5 3 7 2 3
                3 7 1 6 1
                7 2 5 3 4
                4 3 6 4 1
                8 7 3 5 2
        output: 10
    @ Start day: 19. 10. 10
    @ End day: 19. 10. 10
'''

a = [[5, 3, 7, 2, 3],
    [3, 7, 1, 6, 1],
    [7, 2, 5, 3, 4],
    [4, 3, 6, 4, 1],
    [8, 7, 3, 5, 2]]

map = [[0] * 50 for _ in range(50)]

for i in range(1, len(a)):
    for j in range(1, len(a[0])):
        map[i][j] = a[][i]
print(map)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

for y in range(1, len(a)):            # y좌표
    for x in range(1, len(a[0])):     # x좌표
        flag = 0

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            #print(xx, yy)
            #print(map[yy][xx])
            #print(map[1][1])
            if map[y][x] < map[yy][xx]:
                flag = 1
                break


        if flag == 0:
            print(x, y)
            cnt += 1

print(cnt)
