"""
    @ Baek 2711 오타맨 고창영
    @ Prob. https://www.acmicpc.net/problem/2711
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for _ in range(int(input())):
    i, inputStr = map(str, input().split())
    inputStr = list(inputStr)
    inputStr.pop(int(i)-1)
    print("".join(inputStr))

"""
4
4 MISSPELL
1 PROGRAMMING
7 CONTEST
3 BALLOON
>
MISPELL
ROGRAMMING
CONTES
BALOON
"""