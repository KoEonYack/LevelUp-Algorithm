"""
    @ Baek 11098 첼시를 도와줘!
    @ Prob. https://www.acmicpc.net/problem/11098
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for _ in range(int(input())):
    price = 0
    name = ""
    for _ in range(int(input())):
        p, n = map(str, input().split())
        if int(p) > price:
            price = int(p)
            name = n
    print(name)

"""
2
3
10 Iversen
1000000 Nannskog
2000000 Ronaldinho
2
1000000 Maradona
999999 Batistuta
>
Ronaldinho
Maradona
"""
