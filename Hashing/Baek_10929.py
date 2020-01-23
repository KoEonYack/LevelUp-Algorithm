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
hexdigest = hashlib.sha224(encoding_string).hexdigest()
print(hexdigest)


"""
Baekjoon
>
880ceaa24e932e5c19350adc50535922ead12ba689a7a6a9a895d2ce
"""
