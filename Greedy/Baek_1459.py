"""
    @ 1459. 걷기
    @ Prob. https://www.acmicpc.net/problem/1459
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

# W: 한 블록 가는데 걸리는 시간
# S: 가로지르는데 걸리는 시간
X, Y, W, S = map(int, input().split())
if X < Y:
    X, Y = Y, X

mod = (X + Y) % 2
case1 = (X+Y) * W
case2 = Y*S + (X-Y)*W
case3 = (X-mod)*S+mod*W

print(min(case1, case2, case3))


"""
4 2 3 10
>
18

10 10 100 1
>
10

1 10 100 2

"""