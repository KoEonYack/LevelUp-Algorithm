"""
    @ Baek 1292 쉽게 푸는 문제
    @ Prob. https://www.acmicpc.net/problem/1292
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

A, B = map(int, input().split())

MAX_VAL = 100
arr = []
for i in range(1, MAX_VAL):
    arr += [i] * i

#print(arr)
#print(arr[:B])
#print(arr[:A-1])
print(sum(arr[:B]) - sum(arr[:A-1]))



"""
3 7
>
15
"""