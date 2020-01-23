"""
    @ 10931 SHA-384
    @ Prob. https://www.acmicpc.net/problem/10931
     Ref.
    @ Algo: Hashing
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""

import hashlib
inputStr = str(input())
encoded_string = inputStr.encode()
print(hashlib.sha512(encoded_string).hexdigest())


"""
Baekjoon
>
8f077fa785396c86c7f9b8ba03fc41e9ac250a0a3884a2ef5c70638e1a153407b52a58b897a89a0361f2c60c2dc123be
"""