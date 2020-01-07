"""
    @ Baek 2490 윷놀이
    @ Prob. https://www.acmicpc.net/problem/2490
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

# 1 top | 0 bottom
# 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E


def check(arr):
    num_of_zero = arr.count(0)
    if num_of_zero == 0:
        print("E")
    elif num_of_zero == 1:
        print("A")
    elif num_of_zero == 2:
        print("B")
    elif num_of_zero == 3:
        print("C")
    elif num_of_zero == 4:
        print("D")


for i in range(3):
    arr = list(map(int, input().split()))
    check(arr)

"""
0 1 0 1
1 1 1 0
0 0 1 1
>
B
A
B
"""