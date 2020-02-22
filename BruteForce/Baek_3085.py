"""
    @ 3085. 사탕 게임
    @ Prob. https://www.acmicpc.net/problem/3085
     Ref.
    @ Algo: B
    @ Start day: 20. 02. 19.
    @ End day: 20. 02. 19.
"""

def check():
    ans = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if MAP[i][j-1] == MAP[i][j]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

        cnt = 1
        for j in range(1, N):
            if MAP[j - 1][i] == MAP[j][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

    return ans


N = int(input())
MAP = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            MAP[i][j], MAP[i][j+1] = MAP[i][j+1], MAP[i][j]
            tmp = check()
            if tmp > ans:
                ans = tmp
            MAP[i][j+1], MAP[i][j] = MAP[i][j], MAP[i][j+1]

        if i + 1 < N:
            MAP[i][j], MAP[i+1][j] = MAP[i+1][j], MAP[i][j]
            tmp = check()
            if tmp > ans:
                ans = tmp
            MAP[i+1][j], MAP[i][j] = MAP[i][j], MAP[i+1][j]

print(ans)

"""
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
>
4
"""