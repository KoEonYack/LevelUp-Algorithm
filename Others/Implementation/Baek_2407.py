"""
    @ Baek 2407 조합
    @ Prob. https://www.acmicpc.net/problem/2407
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

from math import factorial

N, M = map(int, input().split())
print(factorial(N) // (factorial(M)*factorial(N-M)))


"""
100 6
>
1192052400
"""