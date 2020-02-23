"""
    @ 6064. 카잉 달력
    @ Prob. https://www.acmicpc.net/problem/6064
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 02. 23.
    @ End day: 20. 02. 23.
"""

T = int(input())
for _ in range(T):
    M, N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    STEP = X
    while STEP < N * M:
        if STEP % N == Y:
            print(STEP+1)
            break
        STEP += M
    else:
        print(-1)


"""
1
5 7 3 5
>
33

1
13 11 5 6
>
33

1
10 12 7 2
>

3
10 12 3 9
10 12 7 2
13 11 5 6
>
33
-1
83
"""