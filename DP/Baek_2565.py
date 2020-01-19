"""
    @ 2565. 전깃줄
    @ Prob. https://www.acmicpc.net/problem/2565
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 18.
    @ End day: 20. 01. 18.
"""


N = int(input())
arr = [0]
maxV = 0
for _ in range(N):
    A, B = map(int, input().split())
    arr.append(B)
    if maxV < A:
        maxV = A

arr.sort()

dp = [0] * (maxV+1)

dp[1] = 1
for i in range(2, N+1):
    for j in range(1, i):
        #print(i, j)
        if arr[j] <= arr[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] == 0:
            dp[i] += 1

print(dp)
print(N - max(dp))



"""
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
>
3
"""