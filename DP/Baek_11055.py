"""
    @ 11055. 가장 큰 증가 부분 수열
    @ Prob. https://www.acmicpc.net/problem/11055
     Ref. https://wootool.tistory.com/97
    @ Algo: DP
    @ Start day: 20. 01. 18.
    @ End day: 20. 01. 18.
"""


N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (N+1)

dp[1] = arr[1]
for i in range(2, N+1):
    maxV = 0
    for j in range(1, i):
        if arr[j] < arr[i]:
            if dp[j] > maxV:
                maxV = dp[j]
        dp[i] = maxV + arr[i]
        if dp[i] == 0:
            dp[i] = arr[i]

print(max(dp))

"""
10
1 100 2 50 60 3 5 6 7 8
>
113
"""
