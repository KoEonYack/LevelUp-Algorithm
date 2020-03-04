"""
    @ Baek 2744 대소문자 바꾸기
    @ Prob. https://www.acmicpc.net/problem/2744
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

inputStr = input()

for ch in inputStr:
    if ch.isupper():
        print(ch.lower(), end="")
    else:
        print(ch.upper(), end="")

"""
WrongAnswer
>
wRONGaNSWER
"""
