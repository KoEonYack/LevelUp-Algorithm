"""
    @ 9251. LCS
    @ Prob. https://www.acmicpc.net/problem/9251
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 31.
    @ End day: 20. 01. 31.
"""

X = input()
Y = input()
m = len(X)
n = len(Y)

LCSTable = [[0]*(n+1) for _ in range(m+1)]

for i in range(0, m+1):
    LCSTable[i][0] = 0

for i in range(0, n+1):
    LCSTable[0][i] = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if X[i-1] == Y[j-1]:
            LCSTable[i][j] = LCSTable[i-1][j-1] + 1
        else:
            LCSTable[i][j] = max(LCSTable[i-1][j], LCSTable[i][j-1])

print(LCSTable[m][n])


"""
AA
BBB

ACAYKP
CAPCAK
>
4
"""