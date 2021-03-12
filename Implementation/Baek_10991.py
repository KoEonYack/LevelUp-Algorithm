"""
    @ Baek 10991 별 찍기 - 16
    @ Prob. https://www.acmicpc.net/problem/10991
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

N = int(input())

patt = 0
for i in range(N, 0, -1):
    print(" " * (i - 1) + "*", end="")
    print(" *" * patt)
    patt += 1


"""
4
>
   *
  * *
 * * *
* * * *
"""
