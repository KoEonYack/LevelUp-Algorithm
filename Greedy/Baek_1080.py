"""
    @ Baek 1080. 행렬
    @ Prob. https://www.acmicpc.net/problem/1080
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 04. 20.
    @ End day: 20. 04. 20.
"""
# N: 세로, M: 가로
N, M = map(int, input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

def Flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

def checkEquality():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            Flip(i, j)
            cnt += 1

if checkEquality():
    print(cnt)
else:
    print(-1)


"""
3 4
0000
0010
0000
1001
1011
1001
>
2

"""