"""
    @ 9465. 스티커
    @ Prob. https://www.acmicpc.net/problem/9465
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 19.
    @ End day: 20. 02. 19.
"""

T = int(input())
for _ in range(T):
    N = int(input())
    t1 = [0] + list(map(int, input().split()))
    t2 = [0] + list(map(int, input().split()))
    arr = list(zip(t1, t2))
    DP = [[0]*(3) for _ in range(N+1)]

    for i in range(1, N+1):
        DP[i][0] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2])
        DP[i][1] = max(DP[i-1][0], DP[i-1][2]) + arr[i][0]
        DP[i][2] = max(DP[i-1][0], DP[i-1][1]) + arr[i][1]

    #for a in DP:
    #    print(a)

    print(max(DP[N]))

"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
>
260
290
"""
