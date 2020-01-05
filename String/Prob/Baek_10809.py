'''
    @ Baek 10809
    @ Prob. https://www.acmicpc.net/problem/10809
      Ref.
      Ref Prob.
    @ Algo: String
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
'''


inputArr = list(input())

for i in range(26):
    if chr(97 + i) in inputArr:
        print(inputArr.index(chr(97 + i)), end=" ")
    else:
        print(-1, end=" ")

"""
baekjoon
>
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
"""