"""
    @ 16194. 카드 구매하기 2
    @ Prob. https://www.acmicpc.net/problem/16194
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
        #print(P[i], DP[i-j] + P[j])
        #print(DP)
        if DP[i] > 0:
            DP[i] = min(P[i], DP[i-j] + P[j], DP[i])
        else:
            DP[i] = min(P[i], DP[i-j] + P[j])

print(DP[-1])

"""
4
1 5 6 7
>
4

5
10 9 8 7 6
>
6

10
5 10 11 12 13 30 35 40 45 47
>
26

10
1 1 2 3 5 8 13 21 34 55
>
5
"""

