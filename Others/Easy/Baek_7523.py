"""
    @ Baek 7523 Gauß
    @ Prob. https://www.acmicpc.net/problem/7523
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

for _ in range(int(input())):
    A, B = map(int, input().split())
    resA = ((abs(A) + 1) * abs(A)) / 2
    resB = int(((abs(B) + 1) * abs(B)) / 2)

    if A < 0:
        resA = -resA
    elif B < 0:
        resB = -resB

    print(resA + resB)


"""
3
1 100
-11 10
-89173 938749341
>
Scenario #1:
5050

Scenario #2:
-11

Scenario #3:
440625159107385260

"""
