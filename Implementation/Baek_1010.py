"""
    @ Baek 1010 다리 놓기
    @ Prob. https://www.acmicpc.net/problem/1010
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""
#MAX_SIZE = 31
MAX_SIZE = 10
DP = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]

for i in range(1, MAX_SIZE):
    DP[1][i] = i

for i in range(2, MAX_SIZE):
    for j in range(i, MAX_SIZE):
        for k in range(j, i-1, -1):
            DP[i][j] += DP[j-1][k-1]

for a in DP:
    print(a)

for _ in range(int(input())):
    X, Y = map(int, input().split())
    print(DP[X][Y])

"""
3
2 2
1 5
13 29
>
1
5
67863915
"""