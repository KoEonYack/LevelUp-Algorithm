"""
    @ Baek 10996 별 찍기 - 21
    @ Prob. https://www.acmicpc.net/problem/10996
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""

N = int(input())
if N == 1:
    print("*")
else:
    type1 = "* " * (N//2 + N%2)
    type2 = " *" * (N//2)
    for i in range(N*2):
        if i % 2 == 0:
            print(type1)
        else:
            print(type2)

"""
4
>
* *
 * *
* *
 * *
* *
 * *
* *
 * *
"""