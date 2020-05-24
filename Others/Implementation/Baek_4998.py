"""
    @ Baek 4998 저금
    @ Prob. https://www.acmicpc.net/problem/4998
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 24.
    @ End day: 20. 05. 24.
"""


try:
    while 1:
        A, B, C = map(float, input().split())
        year = 0
        B = B / 100
        while A < C:
            A += A * B
            year += 1
        print(year)
except:
    exit()

"""
200.00 6.5 300
500 4 1000.00
>
7
18
"""