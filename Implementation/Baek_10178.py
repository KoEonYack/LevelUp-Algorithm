"""
    @ Baek 10178 할로윈의 사탕
    @ Prob. https://www.acmicpc.net/problem/10178
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for _ in range(int(input())):
    total, div = map(int, input().split())
    print("You get " + str(total//div) + " piece(s) and your dad gets "+ str(total%div) +" piece(s).")

"""
5
22 3
15 5
99 8
7 4
101 5
>
You get 7 piece(s) and your dad gets 1 piece(s).
You get 3 piece(s) and your dad gets 0 piece(s).
You get 12 piece(s) and your dad gets 3 piece(s).
You get 1 piece(s) and your dad gets 3 piece(s).
You get 20 piece(s) and your dad gets 1 piece(s).
"""