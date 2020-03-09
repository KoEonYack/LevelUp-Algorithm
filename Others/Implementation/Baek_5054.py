"""
    @ Baek 5054 주차의 신
    @ Prob. https://www.acmicpc.net/problem/5054
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 06.
    @ End day: 20. 03. 06.
"""


for _ in range(int(input())):
    N = int(input())
    arr = []
    arr = list(map(int, input().split()))
    arr.sort()
    print((arr[-1] - arr[0]) * 2)


"""
2
4
24 13 89 37
6
7 30 41 14 39 42
>
152
70
"""
