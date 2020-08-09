"""
    @ Baek 10422. 괄호
    @ Prob. https://www.acmicpc.net/problem/10422
     Ref.
    @ Algo: DP
    @ Start day: 20. 08. 09.
    @ End day: 20. 08. 09.
"""

import sys
input = sys.stdin.readline

dp = [0] * 5001
dp[0] = 1
for i in range(2, 5001, 2):
    for j in range(2, i + 1, 2):
        dp[i] += (dp[j - 2] * dp[i - j]) % 1000000007

for i in range(int(input())):
    print(dp[int(input())] % 1000000007)

"""
3
1
2
4
>
0
1
2
"""