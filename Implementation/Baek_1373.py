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
dec = int(n,2)
_oct = oct(dec)
print(_oct[2:].rstrip('L'))

"""
11001100
>
314
"""