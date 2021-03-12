"""
    @ Baek 2953 나는 요리사다
    @ Prob. https://www.acmicpc.net/problem/2953
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

data = []

max_V = 0
max_i = 1
for i in range(1, 6):
    arr = list(map(int, input().split()))
    if sum(arr) > max_V:
        max_V = sum(arr)
        max_i = i

print(max_i, max_V)



"""
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5
>
4 19
"""