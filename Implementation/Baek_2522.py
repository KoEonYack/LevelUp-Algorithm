"""
    @ Baek 2522 별 찍기 - 12
    @ Prob. https://www.acmicpc.net/problem/2522
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

N = int(input())

for i in range(N, 0, -1):
    print(" " * (i-1) + "*" * (N-i+1))

for i in range(1, N):
    print(" " * (i) + "*" * (N-i))


"""
3
>
  *
 **
***
 **
  *
"""


