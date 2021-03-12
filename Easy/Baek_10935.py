"""
    @ 백준 10935 BASE64 인코딩
    @ https://www.acmicpc.net/problem/10935
    @ End Day : 2020. 01. 29.
"""

import base64

plain_str = input()
b = plain_str.encode("UTF-8")
e = base64.b64encode(b)
s = e.decode("UTF-8")
print(s)


"""
Baekjoon
>
QmFla2pvb24=
"""