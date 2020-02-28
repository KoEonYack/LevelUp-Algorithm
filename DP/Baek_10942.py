"""
    @ 10942. 팰린드롬?
    @ Prob. https://www.acmicpc.net/problem/10942
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 28.
    @ End day: 20. 02. 28.
"""
MAX_SIZE = 8
A = [0] + list(map(int, input().split()))
DP = [[False] * (MAX_SIZE + 1) for _ in range(MAX_SIZE+1)]

for i in range(1, MAX_SIZE+1):
    DP[i][i] = True

for i in range(1, MAX_SIZE):
    for j in range(1, MAX_SIZE):
        if A[i-1] == A[j] and i - 1 == j:
            DP[i][j] = True
        elif A[i] == A[j] and abs(i-j) >= 2:
            DP[i][j] = True

for a in DP:
    print(a)

"""
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
>
1
0
1
1
-----------
"""