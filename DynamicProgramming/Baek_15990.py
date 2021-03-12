"""
    @ 15990. 1, 2, 3 더하기 5
    @ Prob. https://www.acmicpc.net/problem/15990
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 14.
    @ End day: 20. 02. 14.
"""

mod = 1000000009
tmp = int(input())
arr = []
for i in range(tmp):
    arr.append(int(input()))


N = max(arr)
DP = [[0] * (4) for _ in range(N+1)]

DP[1][1] = 1
DP[1][2] = 0
DP[1][3] = 0

DP[2][1] = 0
DP[2][2] = 1
DP[2][3] = 0

DP[3][1] = 1
DP[3][2] = 1
DP[3][3] = 1


for i in range(4, N+1):
    DP[i][1] = (DP[i-1][2] + DP[i-1][3]) % mod
    DP[i][2] = (DP[i-2][1] + DP[i-2][3]) % mod
    DP[i][3] = (DP[i-3][1] + DP[i-3][2]) % mod


#for i in range(len(DP)):
#    print(i, DP[i])

for num in arr:
    print(sum(DP[num]) % 1000000009)



"""
1
4
>
3
--------------------------
3
4
7
10
>
3
9
27
"""