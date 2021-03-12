"""
    @ Baek 10992 별 찍기 - 17
    @ Prob. https://www.acmicpc.net/problem/10992
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

N = int(input())

for i in range(N, 1, -1):
    print(" " * (i - 1) + "*", end="")
    print(" " * (2*(N-i) - 1), end="")
    if i != N:
        print("*")
    else:
        print()
print("*" * (2 * N - 1))

"""
  *
 * *
*****
>
3
------------------------
   *
  * *
 *   *
*******
>
4
"""