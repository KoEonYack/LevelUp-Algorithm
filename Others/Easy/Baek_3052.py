"""
    @ Baek 3052 나머지
    @ Prob. https://www.acmicpc.net/problem/3052
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

arr = []
for i in range(10):
    num = int(input())
    mod_num = num % 42
    if mod_num not in arr:
        arr.append(mod_num)

print(len(arr))


"""
39
40
41
42
43
44
82
83
84
85
>
6
"""