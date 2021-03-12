"""
    @ Baek 2445 별 찍기 - 8
    @ Prob. https://www.acmicpc.net/problem/2445
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 23
    @ End day: 20. 01. 23
"""

N = int(input())

for i in range(1, N+1):
    print("*" * i, end="")
    print(" " * 2 * (N-i), end="")
    print("*" * i)

for i in range(N-1, 0, -1):
    print("*" * i, end="")
    print(" " * 2 * (N-i), end="")
    print("*" * i)


"""
5
>

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""