"""
    @ Baek 1652 누울 자리를 찾아라
    @ Prob. https://www.acmicpc.net/problem/1652
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 07.
    @ End day: 20. 04. 07.
"""

N = int(input())
MAP = [list(input()) for _ in range(N)]

# for a in MAP:
#     print(a)

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if MAP[i][j] == '.':
            cnt += 1
        if MAP[i][j] == 'X' and cnt >= 2:
            ans += 1
            cnt = 0
        elif MAP[i][j] == 'X':
            cnt = 0

    if cnt >= 2:
        ans += 1

print(ans, end=" ")

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if MAP[j][i] == '.':
            cnt += 1
        if MAP[j][i] == 'X' and cnt >= 2:
            # print(j, i)
            ans += 1
            cnt = 0
        elif MAP[j][i] == 'X':
            cnt = 0

    if cnt >= 2:
        # print("here", j, i)
        ans += 1

print(ans)



"""
5
....X
..XX.
.....
.XX..
X....
>
5 4
"""