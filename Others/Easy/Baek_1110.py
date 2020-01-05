"""
    @ Baek 1549 평균
    @ Prob. https://www.acmicpc.net/problem/1549
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

ori_num = int(input())
check_num = ori_num
change_num = 0
ans = 0

while True:
    temp = ori_num // 10 + ori_num % 10
    change_num = (ori_num % 10) * 10 + temp % 10
    ans += 1
    ori_num = change_num
    if change_num == check_num:
        break

print(ans)

"""
26
>
4
"""