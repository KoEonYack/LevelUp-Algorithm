"""
    @ Baek 4153 직각삼각형
    @ Prob. https://www.acmicpc.net/problem/4153
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""


arr = list(map(int, input().split()))
while arr[0] != 0 and arr[1] != 0 and arr[2] != 0:
    maxV = max(arr[0], arr[1], arr[2])
    arr.remove(maxV)
    if pow(maxV, 2) == pow(arr[0], 2) + pow(arr[1], 2):
        print("right")
    else:
        print("wrong")
    arr = list(map(int, input().split()))

"""
6 8 10
25 52 60
5 12 13
0 0 0
>
right
wrong
right
"""