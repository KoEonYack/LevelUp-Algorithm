"""
    @ Baek 2587 대표값2
    @ Prob. https://www.acmicpc.net/problem/2587
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

arr = [int(input()) for i in range(5)]
arr.sort()
print(int(sum(arr) / 5))
print(arr[2])

"""
10
40
30
60
30
>
34
30
"""


