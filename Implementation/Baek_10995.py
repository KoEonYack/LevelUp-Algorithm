"""
    @ Baek 10995 별 찍기 - 20
    @ Prob. https://www.acmicpc.net/problem/10995
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

N = int(input())
for i in range(N):
    if i % 2 == 0:
        print("* " * N)
    else:
        print(" ", end="")
        print("* " * N)


"""
2
>
* *
 * *
 
"""