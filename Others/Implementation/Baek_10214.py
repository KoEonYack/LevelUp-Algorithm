"""
    @ Baek 10214 Baseball
    @ Prob. https://www.acmicpc.net/problem/10214
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

for _ in range(int(input())):
    K = Y = 0
    for _ in range(9):
        y, k = map(int, input().split())
        K += k
        Y += y

    if K > Y:
        print("Korea")
    elif K < Y:
        print("Yonsei")
    else:
        print("Draw")


"""
1
1 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
>
Yonsei
"""
