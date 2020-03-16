"""
    @ Baek 10420 기념일 1
    @ Prob. https://www.acmicpc.net/problem/10420
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

import datetime

days = int(input())
dt = datetime.datetime(2014, 4, 2) + datetime.timedelta(days=days-1)
print(dt.strftime("%Y-%m-%d"))

"""
200
>
2014-10-18
"""