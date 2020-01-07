"""
    @ Baek 1924 2007년
    @ Prob. https://www.acmicpc.net/problem/19224
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 07
    @ End day: 20. 01. 07
"""

import datetime

def print_whichdat(M, D):
    r = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    aday = datetime.date(2007, M, D)
    bday = aday.weekday()
    return r[bday]


Month, Day = map(int, input().split())
print(print_whichdat(Month, Day))


"""
1 1
>
MON

3 14
>
WED
"""