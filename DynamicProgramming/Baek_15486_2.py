N = int(input())
T = [0] * N
P = [0] * N
DP = [0] * (N+50)

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N):
    DP[i + T[i]] = max(DP[i+T[i]], DP[i]+P[i])
    DP[i+1] = max(DP[i+1], DP[i])

print(DP[N])

