"""
    @ Baek 10102 개표
    @ Prob. https://www.acmicpc.net/problem/10102
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

N = int(input())
inputStr = input()
numA = inputStr.count("A")
numB = inputStr.count("B")

if numA > numB:
    print("A")
elif numA < numB:
    print("B")
else:
    print("Tie")


"""
6
ABBABB
>
B
"""