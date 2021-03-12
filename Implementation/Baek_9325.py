"""
    @ Baek 9325 얼마?
    @ Prob. https://www.acmicpc.net/problem/9325
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

for _ in range(int(input())):
    carPrice = int(input())
    for _ in range(int(input())):
        num, opPrice = map(int, input().split())
        carPrice += (num * opPrice)
    print(carPrice)


"""
2
10000
2
1 2000
3 400
50000
0
>
13200
50000
"""