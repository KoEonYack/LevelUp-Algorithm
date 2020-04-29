import sys
sys.setrecursionlimit(100000)


DP = [[0] * 10001 for _ in range(10001)]

def partition(n, m):
    count = 0

    if n < m:
        m = n
    if DP[n][m] > 0:
        return DP[n][m]
    if n == 0:
        DP[n][m] = 1
        return 1

    for i in range(1, m+1):
        # print(n-i, i)
        count += partition(n-i, i)

    DP[n][m] = count
    return count


for _ in range(int(input())):
    N = int(input())
    print(partition(N, 3))