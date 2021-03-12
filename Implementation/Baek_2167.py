"""
    @ Baek 2167 2차원 배열의 합
    @ Prob. https://www.acmicpc.net/problem/2167
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

for a in MAP:
    print(a)

for _ in range(int(input())):
    i, j, X, Y = map(int, input().split())
    ans = 0
    for yy in range(j-1, X):
        for xx in range(i-1, Y):
            #print(yy, xx, MAP[yy][xx])
            ans += MAP[yy][xx]
    print(ans)

"""
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
>
63
2
36
"""