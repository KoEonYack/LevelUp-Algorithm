"""
    @ Baek 1717. 집합의 표현
    @ Prob. https://www.acmicpc.net/problem/1717
     Ref.
    @ Algo: Union Find
    @ Start day: 20. 03. 26.
    @ End day: 20. 03 26.
"""

def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x == y:
        return

    if rank[x] < rank[y]: x, y = y, x
    parent[y] = x
    if rank[x] == rank[y]:
        rank[x] = rank[y] + 1


def Find(x):
    if parent[x] == x:
        return x
    else:
        y = Find(parent[x])
        parent[x] = y
        return parent[x]


N, M = map(int, input().split())
rank = [0] * (N+1)
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for _ in range(M):
    C, A, B = map(int, input().split())
    if C == 0:      # 합집합
        a = Find(A)
        b = Find(B)
        if a > b: Union(a, b)
        elif a < b:  Union(b, a)

    elif C == 1:    # 검사
        a = Find(A)
        b = Find(B)
        if a == b:
            print("YES")
        else:
            print("NO")
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
>
NO
NO
YES
"""
