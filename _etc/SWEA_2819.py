'''
    @ 2819. 격자판의 숫자 이어 붙이기
    @ Prob. https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&&&
    @ Algo: DFS
    @ Start day: 19. 09. 02
    @ End day:
'''

#TestNum = int( input() )
TestNum = 1
setOfNum = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def getSum(x, y, cnt, s):
    s += arr[x][y] + '0'
    cnt = cnt + 1
    if cnt is 7:
        setOfNum.add(s)
        print(type(setOfNum))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or 4 <= nx or ny < 0 or 4 <= ny:
            continue
        getSum(nx, ny, cnt, s)

for num in range(TestNum):
    arr = [[col for col in range(4)] for row in range(4)]
    for i in range(4):
        for j in range(4):
            arr[i][j] = input()

    for i in range(4):
        for j in range(4):
            getSum(i, j, 0, "")
    print("# {0} {1}".format(num, len(setOfNum) -1))
