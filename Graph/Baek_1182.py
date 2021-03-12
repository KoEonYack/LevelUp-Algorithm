"""
    @ Baek 1182. 부분수열의 합
    @ Prob. https://www.acmicpc.net/problem/1182
     Ref.
    @ Algo: DFS
    @ Start day: 20. 08. 19.
    @ End day: 20. 08. 19.
"""

def dfs_prev(idx, path):
    res.append(path)

    for i in range(idx, N):
        dfs_prev(i+1, path+[arr[i]])

    return res

ans = 0
def dfs(idx, path):
    global ans

    if len(path) != 0 and sum(path) == S:
        ans += 1

    for i in range(idx, N):
        dfs(i+1, path+[arr[i]])

    return ans


res = []
N, S = map(int, input().split())
arr = list(map(int, input().split()))
# print(dfs_prev(0, []))
print(dfs(0, []))


"""
5 0
-7 -3 -2 5 8
>
1
"""


