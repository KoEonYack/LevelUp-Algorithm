"""
    @ Baek 1252 이진수 덧셈
    @ Prob. https://www.acmicpc.net/problem/1252
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

A, B = map(str, input().split())
sum_digit = int(A, 2) + int(B, 2)
print(bin(sum_digit)[2:])

"""
1001101 10010
>
1011111

"""