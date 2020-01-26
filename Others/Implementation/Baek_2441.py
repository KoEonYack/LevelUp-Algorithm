"""
    @ Baek 2441 별 찍기 - 4
    @ Prob. https://www.acmicpc.net/problem/2441
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

N = int(input())
for i in range(N, 0, -1):
    print(" " * (N-i) + "*" * i)


"""
5
>
*****
 ****
  ***
   **
    *
"""