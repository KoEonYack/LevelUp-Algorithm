"""
    @ 10928 SHA-512
    @ Prob. https://www.acmicpc.net/problem/10928
     Ref. https://has3ong.tistory.com/556
    @ Algo: Hashing
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

import hashlib

inputStr = input()
encoding_string = inputStr.encode()
hexdigest = hashlib.sha1(encoding_string).hexdigest()
print(hexdigest)


"""
Baekjoon
>
a25cdb0b8ead2861a3ef2c48cdc15517994ab278
"""
