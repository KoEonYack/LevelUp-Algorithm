"""
    @ 11060. 점프 점프
    @ Prob. https://www.acmicpc.net/problem/11060
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 28.
    @ End day: 20. 02. 28.
"""

N = int(input())
A = [0] + list(map(int, input().split()))
DP = [999999] * 2 * (N+1)

DP[0] = 0
DP[1] = 0
for i in range(1, N+1):
    for j in range(i, i+A[i]+1):
        #print(i + A[i] + 1)
        if i < N + 1:
            DP[j] = min(DP[i] + 1, DP[j])

#print(DP[:N+1])
if DP[N] == 999999:
    print(-1)
else:
    print(DP[N])


"""
10
1 2 0 1 3 2 1 5 4 2
>
5
"""