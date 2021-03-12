"""
    @ Baek 2292 벌집
    @ Prob. https://www.acmicpc.net/problem/2292
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 15
    @ End day: 20. 01. 15
"""


def solution(Num):
    if Num == 1:
        return 1

    Num -= 1
    idx = 1
    while True:
        Num -= (idx * 6)
        if Num <= 0:
            return idx + 1
        idx += 1


N = int(input())
print(solution(N))


"""
13
>
3
"""
