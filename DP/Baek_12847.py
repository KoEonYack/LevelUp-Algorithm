"""
    @ Baek 12847 꿀 아르바이트
    @ Prob. https://www.acmicpc.net/problem/12847
      Ref.
      Ref Prob.
    @ Algo: DP
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
res = sum(arr[1:M+1])
#print(res)
for i in range(M+1, N+1):
    # print(i)
    if res < res - arr[i] + arr[i-M]:
        res = res - arr[i] + arr[i-M]

print(res)

"""
5 3
10 20 30 20 10
>
70
"""