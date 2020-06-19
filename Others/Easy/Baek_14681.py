"""
    @ Baek 14681. 사분면 고르기
    @ https://www.acmicpc.net/problem/14681
    @ End Day : 2020. 06. 19.
"""

A = int(input())
B = int(input())

if A > 0 and B > 0:
    print(1)
elif A < 0 and B > 0:
    print(2)

elif A < 0 and B < 0:
    print(3)

else:
    print(4)

"""
9
-13
"""