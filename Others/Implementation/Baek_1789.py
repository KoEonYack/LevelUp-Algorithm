"""
    @ Baek 1789 수들의 합
    @ Prob. https://www.acmicpc.net/problem/1789
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""


Target = int(input())
cul_sum = 0
i = 0
ans = 0
while True:
    i += 1
    cul_sum += i
    ans += 1
    if cul_sum > Target:
        print(ans - 1)
        break


"""
200
>
19
"""

