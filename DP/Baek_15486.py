"""
    @ 15486. 퇴사 2
    @ Prob. https://www.acmicpc.net/problem/15486
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 28.
    @ End day: 20. 02. 28.
"""

N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

DP = [0] * (N + 50)
for i in range(N):
    DP[i + T[i]] = max(DP[i] + P[i], DP[i + T[i]])
    DP[i+1] = max(DP[i+1], DP[i])

#print(DP)
print(DP[N])

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
>
45
--------------
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
>
55
----------------
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
>
20

"""
