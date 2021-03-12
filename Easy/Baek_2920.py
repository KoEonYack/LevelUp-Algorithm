"""
    @ Baek 2920 숫자의 개수
    @ Prob. https://www.acmicpc.net/problem/2920
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

inputArr = list(map(int, input().split()))

if inputArr == sorted(inputArr):
    print('ascending')
elif inputArr == sorted(inputArr, reverse=True):
    print('descending')
else:
    print('mixed')

"""
1 2 3 4 5 6 7 8
>
ascending

8 1 7 2 6 3 5 4
>
mixed
"""
