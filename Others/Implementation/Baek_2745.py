"""
    @ Baek 2745 진법 변환
    @ Prob. https://www.acmicpc.net/problem/2745
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 24.
    @ End day: 20. 02. 24.
"""

import math

inputStr, base = map(str, input().split())
base = int(base)
i = 0
ans = 0
for ch in inputStr[::-1]:
    if 'A' <= ch <= 'Z':
        ans += (ord(ch) - 55) * pow(base, i)
    elif ch.isdigit():
        ans += int(ch) * pow(base, i)
    i += 1

print(ans)

"""
ZZZZZ 36
>
60466175
"""