"""
    @ Baek 2443 별 찍기 - 6
    @ Prob. https://www.acmicpc.net/problem/2443
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""

N = int(input())

for i in range(N, 0, -1):
    print(" " * (N-i), end="")
    print("*" * (2*i - 1))


"""
5
>
*********
 *******
  *****
   ***
    *

"""