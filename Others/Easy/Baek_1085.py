"""
    @ Baek 1085 직사각형에서 탈출
    @ Prob. https://www.acmicpc.net/problem/1085
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

curX, curY, W, H = map(int, input().split())

step = min(curX, W-curX)
step = min(step, min(curY, H-curY))
print(step)

"""
6 2 10 3
>
1
"""