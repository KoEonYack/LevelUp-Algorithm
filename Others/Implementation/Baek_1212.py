"""
    @ Baek 1373 2진수 8진수
    @ Prob. https://www.acmicpc.net/problem/1373
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

n = input()
dec = int(n,8)
_bin = bin(dec)
print(_bin[2:].rstrip('L'))

"""
314
>
11001100
"""