"""
Note.
      1 2 3 4 5 6 7 8
    ------------------
arr = 5 3 7 8 6 2 9 4

dy =
dy[7] = 9가 증가수열의 마지막 항이면서 가장 긴 수열의 길이

    @ 4. 최대 부분 증가수열
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (N+1)

dp[1] = 1
for i in range(2, N+1):
    for j in range(1, i):
        #print(i, j)
        if arr[j] < arr[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] == 0:
            dp[i] += 1

print(max(dp))

"""
6
10 20 10 30 20 50
>
4
"""
