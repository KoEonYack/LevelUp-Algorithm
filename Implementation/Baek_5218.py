"""
    @ Baek 5218 알파벳 거리
    @ Prob. https://www.acmicpc.net/problem/5218
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""


for _ in range(int(input())):
    A, B = map(str, input().split())
    print("Distances: ", end="")
    for i in range(len(A)):
        if ord(B[i]) - ord(A[i]) >= 0:
            print(ord(B[i]) - ord(A[i]), end=" ")
        else:
            print(26 + (ord(B[i]) - ord(A[i])), end=" ")

    print()


"""
5
AAAA ABCD
ABCD AAAA
DARK LOKI
STRONG THANOS
DEADLY ULTIMO
>
Distances: 0 1 2 3
Distances: 0 25 24 23
Distances: 8 14 19 24
Distances: 1 14 9 25 1 12
Distances: 17 7 19 5 1 16
"""