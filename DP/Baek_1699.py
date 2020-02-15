"""
    @ 1699. 제곱수의 합
    @ Prob. https://www.acmicpc.net/problem/1699
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 14.
    @ End day: 20. 02. 14.
"""

N = int(input())
DP = [0] * (N+1)

for i in range(1, N+1):
    DP[i] = i
    j = 1
    while j*j <= i:
        if DP[i] > DP[i-j*j] + 1:
            DP[i] = DP[i-j*j] + 1
        j += 1

print(DP[N])


"""
7
>
4
"""