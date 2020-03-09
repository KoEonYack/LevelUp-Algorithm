"""
    @ 백준 10156 과자
    @ https://www.acmicpc.net/problem/10156
    @ End Day : 2020. 03. 09.
"""

CP, C, P = map(int, input().split())
if CP * C >= P:
    print(CP * C - P)
else:
    print(0)

"""
300 4 1000
>
200
"""