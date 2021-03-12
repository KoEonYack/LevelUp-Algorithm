"""
    @ Baek 5635 생일
    @ Prob. https://www.acmicpc.net/problem/5635
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

from datetime import date

d0 = date(2020, 3, 5)
min_name = ""
min_day_delta = 9999999
max_day_delta = -1
max_name = ""

for _ in range(int(input())):
    name, D, M, Y = map(str, input().split())

    d1 = date(int(Y), int(M), int(D))
    if (d0-d1).days < min_day_delta:
        min_day_delta = (d0 - d1).days
        min_name = name
    elif (d0-d1).days > max_day_delta:
        max_day_delta = (d0 - d1).days
        max_name = name


print(min_name)
print(max_name)


"""
5
Mickey 1 10 1991
Alice 30 12 1990
Tom 15 8 1993
Jerry 18 9 1990
Garfield 20 9 1990
>
Tom
Jerry
"""