"""
    @ 백준 10938 BASE32 인코딩
    @ https://www.acmicpc.net/problem/10938
    @ End Day : 2020. 01. 29.
"""

import base64

s1 = input()
b1 = s1.encode("UTF-8")
d = base64.b32encode(b1)
s = d.decode("UTF-8")
print(s)


"""
Baekjoon
>
IJQWK23KN5XW4===
"""