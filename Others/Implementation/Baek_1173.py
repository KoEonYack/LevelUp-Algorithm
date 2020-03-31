"""
    @ Baek 1173 운동
    @ Prob. https://www.acmicpc.net/problem/1158
      Ref.
      Ref Prob.
    @ Algo: 구현(큐)
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""

import sys

# N(운동 횟수) mm(하한선) M(상한선) T(맥박 증가) R(감소치)
N, mm, M, T, R = map(int, input().split())

cnt = 0
num_exercise = 0
curr = mm
while num_exercise != N:
    if curr + T <= M: # 운동을 할 수 있는 경우
        curr += T
        num_exercise += 1
    else:             # 운동 해야함
        if curr - R < mm:
            curr = mm
        else:
            curr -= R
    if curr + T > M and curr == mm:
        print(-1)
        sys.exit()

    cnt += 1

print(cnt)

"""
5 70 120 25 15
>
10
"""