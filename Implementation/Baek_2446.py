"""
    @ Baek 2446 별 찍기 - 9
    @ Prob. https://www.acmicpc.net/problem/2446
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""

N = int(input())

for i in range(N, 0, -1):
    print(" " * (N - i), end="")
    print("*" * (2 * i - 1))

for i in range(2, N+1):
    print(" " * (N - i), end="")
    print("*" * (2 * i - 1))

"""
5
>
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
"""


