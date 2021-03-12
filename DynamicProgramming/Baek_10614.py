"""
    @ 10164. 격자상의 경로
    @ Prob. https://www.acmicpc.net/problem/10164
      Ref.  https://wjdgus2951.tistory.com/15
    @ Algo: DP
    @ Start day: 20. 01. 30.
    @ End day: 20. 01. 30.
"""

# M 세로, N 가로
Y, X, K = map(int, input().split())
cache = [[0]*(X+1) for _ in range(Y+1)]
div_x_idx = -1
div_y_idx = -1
cache[1][1] = 1
cnt = 1

for i in range(1, Y+1):
    for j in range(1, X+1):
        if cnt == K:
            div_x_idx = j
            div_y_idx = i
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
        cnt += 1
        if i == 1 and j == 1: continue
        cache[i][j] = cache[i-1][j] + cache[i][j-1]

if K == 0: print(cache[-1][-1])
else:
    div_sum = cache[div_y_idx][div_x_idx]
    cache = [[0] * (X + 1) for _ in range(Y + 1)]
    cache[div_y_idx][div_x_idx] = 1
    #for a in cache:
    #    print(a)
    for i in range(div_y_idx, Y+1):
        for j in range(div_x_idx, X+1):
            if i == div_y_idx and j == div_x_idx: continue
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    print(div_sum * cache[-1][-1])

#for a in cache:
#    print(a)

"""
3 5 8
>
9
"""
