"""
    @ 10929 MD5
    @ Prob. https://www.acmicpc.net/problem/10929
     Ref. https://has3ong.tistory.com/556
    @ Algo: Hashing
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

import hashlib

inputStr = input()
encoding_string = inputStr.encode()
hexdigest = hashlib.md5(encoding_string).hexdigest()
print(hexdigest)


"""
Baekjoon
>
91bebba139b8b8aee0d8e80e27f473a3
"""
