"""
    @ 15652. N과 M (4)
    @ Prob. https://www.acmicpc.net/problem/15652
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 02. 22.
    @ End day: 20. 02. 22.
"""

a = [0] * 10
c = [False] * 10


def go(idx, start, n, m):
    if idx == m:
        for i in range(0, m):
            print(a[i], end=" ")
        print()
        return

    for i in range(start, n+1):
        c[i] = True
        a[idx] = i
        go(idx+1, i, n, m)
        c[i] = False


n, m = map(int, input().split())
go(0, 1, n, m)

"""
4 2
>
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""

