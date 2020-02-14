"""
    @ 11052. 카드 구매하기
    @ Prob. https://www.acmicpc.net/problem/11052
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 13.
    @ End day: 20. 02. 13.
"""

N = int(input())
P = [0]
P = P + list(map(int, input().split()))
DP = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        DP[i] = max(P[i], DP[i-j] + P[j], DP[i])

print(DP[-1])

"""
4
1 5 6 7
>
10

5
10 9 8 7 6
>
50

10
5 10 11 12 13 30 35 40 45 47
>
50
"""

