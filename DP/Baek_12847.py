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
maxV = res
#print(res)
for i in range(M+1, N+1):
    # print(i)
    res = res + arr[i] - arr[i-M]
    if maxV < res:
        maxV = res

print(maxV)

"""
6 6
10 20 30 20 10 90
>
70
"""