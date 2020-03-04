"""
    @ Baek 1357 뒤집힌 덧셈
    @ Prob. https://www.acmicpc.net/problem/1357
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

x, y = map(str, input().split())
s = str(int(x[::-1]) + int(y[::-1]))
print(s[::-1])

"""
123 100
>
223
"""