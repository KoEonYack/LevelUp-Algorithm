"""
    @ 11057. 오르막 수
    @ Prob. https://www.acmicpc.net/problem/11057
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 19.
    @ End day: 20. 02. 19.
"""

N = int(input())
DP = [[0] * (N+1) for _ in range(10)]
mod = 10007

for i in range(10):
    DP[i][0] = 1

#for a in DP:
#    print(a)

for i in range(1, N+1):
    for j in range(0, 10):
        for k in range(0, j+1):
            DP[j][i] = (DP[j][i] + DP[k][i-1]) % mod

#print("----------")
#for a in DP:
#    print(a)

result = 0
for i in range(10):
    result += DP[i][N-1]

print(result % mod)

"""
1
>
10
-----------
2
>
55
-----------
3
>
220
"""
