"""
    @ 14002. 가장 긴 증가하는 부분 수열 4
    @ Prob. https://www.acmicpc.net/problem/14002
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 14.
    @ End day: 20. 02. 14.
"""

def go(p):
    if p == -1:
        return
    go(visited[p])
    print(arr[p], end=" ")


N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
DP = [0] * (N+1)
visited = [-1] * (N+1)
ans = []
for i in range(1, N+1):
    DP[i] = 1
    for j in range(1, i+1):
        if arr[j] < arr[i] and DP[i] < DP[j] + 1:
            DP[i] = DP[j] + 1
            visited[i] = j

ans = max(DP)
maxIdx = -1
for i in range(len(arr)):
    if DP[i] == ans:
        maxIdx = i

print(ans)
go(maxIdx)



"""
6
10 20 10 30 20 50
>
4
10 20 30 50
-----------------------------------
7
100 30 20 10 50 70 1000
>

"""