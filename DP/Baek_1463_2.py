"""
    @ 1463. 1로 만들기
    @ Prob. https://www.acmicpc.net/problem/1463
     Ref.   https://chunghyup.tistory.com/49
    @ Algo: DP
    @ Start day: 20. 02. 13.
    @ End day: 20. 02. 13.
"""

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1): # 1 ~ N
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2] + 1
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] + 1

print(dp[N])

"""
10
>
3
"""