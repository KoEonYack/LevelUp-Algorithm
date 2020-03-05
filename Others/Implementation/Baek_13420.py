"""
    @ Baek 13420 사칙연산
    @ Prob. https://www.acmicpc.net/problem/13420
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for _ in range(int(input())):
    A, op, B, _, Res = map(str, input().split())
    A = int(A)
    B = int(B)
    Res = int(Res)
    if op == "*":
        if A*B == Res:
            print("correct")
        else:
            print("wrong answer")
    elif op == "/":
        if A/B == Res:
            print("correct")
        else:
            print("wrong answer")
    elif op == "+":
        if A+B == Res:
            print("correct")
        else:
            print("wrong answer")
    elif op == "-":
        if A-B == Res:
            print("correct")
        else:
            print("wrong answer")

"""
4
3 * 2 = 6
11 + 11 = 11
7 - 9 = -2
3 * 0 = 0
>
correct
wrong answer
correct
correct
"""