"""
    @ Baek 11179 2진수 뒤집기
    @ Prob. https://www.acmicpc.net/problem/11179
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

inputVal = bin(int(input()))
binVal = inputVal[2::]
print(int("0b" + binVal[::-1], 2))


"""
13
>
11
----------------
47
>
61
"""