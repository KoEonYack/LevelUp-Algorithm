"""
    @ Baek 5565 영수증
    @ Prob. https://www.acmicpc.net/problem/5565
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

total = int(input())
cul_sum = 0
for _ in range(9):
    cul_sum += int(input())

print(total - cul_sum)

"""
9850
1050
800
420
380
600
820
2400
1800
980
>
600
"""