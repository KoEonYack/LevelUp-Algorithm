"""
    @ Baek 10103 주사위 게임
    @ Prob. https://www.acmicpc.net/problem/10103
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

totalA = totalB = 100

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        totalB -= A
    elif A < B:
        totalA -= B

print(totalA)
print(totalB)


"""
4
5 6
6 6
4 3
5 2
>
94
91
"""