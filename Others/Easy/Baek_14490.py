"""
    백준 14490 백대열
    End Day : 2020. 01. 29.
"""


from math import gcd

A, B = map(int, input().split(":"))
div = gcd(A, B)
print(str(int(A/div)) + ":" + str(int(B/div)))

"""
100:10
>
10:1
------------
18:24
>
3:4
"""