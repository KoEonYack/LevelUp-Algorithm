"""
    @ Baek 5554 심부름 가는 길
    @ Prob. https://www.acmicpc.net/problem/5554
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""

cul_sum = 0
for _ in range(4):
    cul_sum += int(input())

print(cul_sum//60, "\n" + str(cul_sum%60))


"""
31
34
7
151
>
3
43
"""