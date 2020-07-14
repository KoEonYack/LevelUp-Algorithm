"""
    @ Baek 10426.
    @ Prob. https://www.acmicpc.net/problem/16561
     Ref.
    @ Algo: 날짜 모듈
    @ Start day: 20. 07. 14.
    @ End day: 20. 07. 14.
"""

from datetime import timedelta
import datetime

yy, dd = input().split()
Y, M, D = map(int, yy.split("-"))

print(datetime.date(Y, M, D) + datetime.timedelta(days=int(dd)-1))


"""
2014-04-02 1
>
2014-04-03

2014-04-02 200
>
2014-10-18

"""