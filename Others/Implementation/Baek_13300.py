"""
    @ Baek 13300 방 배정
    @ Prob. https://www.acmicpc.net/problem/13300
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 06.
    @ End day: 20. 04. 06.
"""

N, K = map(int, input().split())
S = [[0] * 7 for _ in range(2)]
for _ in range(N):
    x, y = map(int, input().split())
    S[x][y] += 1

# for a in S:
#     print(a)

ans = 0
for i in range(2):
    for j in range(1, 7):
        ans = ans + (S[i][j] // K)
        if S[i][j] % K != 0:
            ans += 1

print(ans)



"""
16 2
1 1
0 1
1 1
0 2
1 2
0 2
0 3
1 3
1 4
1 3
1 3
0 6
1 5
0 5
1 5
1 6
>
12
--------------
3 3
0 3
1 5
0 6
>
3
"""
