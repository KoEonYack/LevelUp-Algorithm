"""
    @ Baek 11060 점프 점프
    @ Prob. https://www.acmicpc.net/problem/11060
      Ref.
      Ref Prob.
    @ Algo: DP
    @ Start day: 20. 09. 08.
    @ End day: 20. 09. 08.
"""

import sys

N = int(input())
arr = [0] + list(map(int, input().split()))
DP = [sys.maxsize] * 2 * (N + 1) 


DP[0] = DP[1] = 0

# for i in range(arr[0]+1):
#     DP[i] = 1

for i in range(1, N+1): 
    for j in range(i, i+arr[i]+1):
        #if i >= N + 1: break
        # print(j, DP[i]+1, DP[j], DP)
        if i < N + 1:
            DP[j] = min(DP[i]+1, DP[j])

if DP[N] == sys.maxsize:
    print(-1)
else:
    print(DP[N])


"""
10
1 2 0 1 3 2 1 5 4 2
>
5
"""