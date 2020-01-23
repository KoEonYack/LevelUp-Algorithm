"""
    @ 10929 SHA-224
    @ Prob. https://www.acmicpc.net/problem/10929
     Ref. https://has3ong.tistory.com/556
    @ Algo: Hashing
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

import hashlib

inputStr = input()
encoding_string = inputStr.encode()
hexdigest = hashlib.sha256(encoding_string).hexdigest()
print(hexdigest)


"""
Baekjoon
>
9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857
"""
