"""
    @ 15651. N과 M (3)
    @ Prob. https://www.acmicpc.net/problem/15651
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 02. 22.
    @ End day: 20. 02. 22.
"""


def go(idx, start, end, m):
    if idx == m:
        print(' '.join(map(str, a)))
        return
    for i in range(start, end+1):
        c[i] = True
        a[idx] = i
        go(idx+1, start, end, m)
        c[i] = False


N, M = map(int, input().split())
c = [False] * (N+1)
a = [0] * M

go(0, 2, N, M)


"""
5 2

4 2
>
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
"""
