"""
    @ Baek 14728. 벼락치기
    @ Prob. https://www.acmicpc.net/problem/14728
      Ref.
    @ Algo: DP(0-1 Knapsack)
    @ Start day: 20. 04. 06.
    @ End day: 20. 04. 06.
"""


N, P = map(int, input().split())
DP = [0] * 10001
for _ in range(N):
    k, s = map(int, input().split())

    i = P
    while i >= k:
        i -= 1
        DP[i] = max(DP[i], DP[i-k] + s)

print(DP[P-1])

"""
3 310
50 40
100 70
200 150
>
220
"""

