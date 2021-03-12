"""
    @ Baek 3460 이진수
    @ Prob. https://www.acmicpc.net/problem/3460
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

for _ in range(int(input())):
    bin_v = bin(int(input()))[2:]
    sep = 0
    for num in bin_v[::-1]:
        if num == "1":
            print(sep, end=" ")
        sep += 1



"""
1
13 -> 1101
>
0 2 3
"""