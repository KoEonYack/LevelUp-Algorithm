"""
    @ Baek 2003. 수들의 합 2
    @ Prob. https://www.acmicpc.net/problem/2003
     Ref.
    @ Algo: DP
    @ Start day: 20. 08. 29.
    @ End day: 20. 08. 29.
"""

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
# DP = [[0] * (N+1) for _ in range(N+1)]

ans = 0
for i in range(1, N+1):
    val = 0
    for j in range(i, N+1):
        val += arr[j]
        if val == M:
            ans += 1

print(ans)

"""
4 2
1 1 1 1
>
3
--------------
10 5
1 2 3 4 2 5 3 1 1 2
>
3
"""