"""
    @ Baek 1526 가장 큰 김만수
    @ Prob. https://www.acmicpc.net/problem/1526
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""


N = input()

while True:
    flag = True
    for n in N:
        if n != "4" and n != "7":
            flag = False
            N = str(int(N)-1)
            break
    if flag is True:
        print(N)
        break

"""
100
>
77
"""
