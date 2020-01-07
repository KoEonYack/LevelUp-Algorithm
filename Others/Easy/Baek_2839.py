"""
    @ Baek 2839 설탕 배달
    @ Prob. https://www.acmicpc.net/problem/2839
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

sugar_w = int(input())
curr_w = 0
i = 0
while 3 * i <= sugar_w:
    curr_w = 3 * i
    if (sugar_w - curr_w) % 5 == 0:
        print(i + (sugar_w - curr_w)//5)
        exit(0)
    i += 1

print(-1)

"""
18
>
4

6
>
2

11
>
3
"""