"""
    @ Baek 10039 평균 점수
    @ Prob. https://www.acmicpc.net/problem/10039
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

total_sum = 0
for _ in range(5):
    num = int(input())
    if num <= 40:
        total_sum += 40
    else:
        total_sum += num

print(int(total_sum / 5))

"""
10
65
100
30
95
>
68
"""