"""
    @ Baek 5717 상근이의 친구들
    @ Prob. https://www.acmicpc.net/problem/5717
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

while True:
    M, G = map(int, input().split())
    if M == G == 0:
        break
    print(M+G)


"""
2 2
2 3
5 5
1 1
0 0
>
4
5
10
2
"""