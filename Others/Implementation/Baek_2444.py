"""
    @ Baek 2444 별 찍기 - 7s
    @ Prob. https://www.acmicpc.net/problem/2444
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""

N = int(input())

for i in range(1, N+1):
    print(" " * (N - i), end="")
    print("*" * (2*i - 1))

for i in range(N-1, 0, -1):
    print(" " * (N - i), end="")
    print("*" * (2*i - 1))


"""
5
>
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""