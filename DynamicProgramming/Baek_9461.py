"""
    @ 9461. 피보나치 수 2
    @ Prob. https://www.acmicpc.net/problem/9461
     Ref.
    @ Algo: Recursion
    @ Start day: 20. 01. 12.
    @ End day: 20. 01. 12.
"""


D = [1, 1, 1, 1, 2, 2]

for i in range(6, 101):
    D.append(D[i-1] + D[i-5])

for _ in range(int(input())):
    print(D[int(input())])

"""
2
6
12
>
3
16
"""
