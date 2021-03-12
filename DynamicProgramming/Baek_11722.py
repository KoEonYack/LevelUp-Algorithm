"""
    @ 11722. 가장 긴 감소하는 부분 수열
    @ Prob. https://www.acmicpc.net/problem/11722
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
DP = [0] * N

for i in range(N):
    DP[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and DP[i] < DP[j] + 1:
            DP[i] = DP[j] + 1

print(max(DP))

"""
6
10 30 10 20 20 10
>
3
"""