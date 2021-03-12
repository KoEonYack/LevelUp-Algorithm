"""
    @ 15988. 1, 2, 3 더하기 3
    @ Prob. https://www.acmicpc.net/problem/15988
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 15.
    @ End day: 20. 02. 15.
"""

DP = [0] * 1000001
DP[1], DP[2], DP[3] = 1, 2, 4
for i in range(4, 1000001):
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 1000000009

for _ in range(int(input())):
    print(DP[int(input())])


"""
3
4
7
10
>
7
44
274
"""