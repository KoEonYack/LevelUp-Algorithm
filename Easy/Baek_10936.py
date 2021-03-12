"""
    @ 백준 10936 BASE64 디코딩
    @ https://www.acmicpc.net/problem/10936
    @ End Day : 2020. 01. 29.
"""

import base64

base64_str = input()

d = base64.b64decode(base64_str)
s = d.decode("UTF-8")
print(s)


"""
QmFla2pvb24=
>
Baekjoon
"""