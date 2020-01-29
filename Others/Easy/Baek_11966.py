"""
    @ 백준 11966 2의 제곱인가?
    @ https://www.acmicpc.net/problem/11966
    @ End Day : 2020. 01. 29.
"""

N = int(input())
squares = [2**i for i in range(31)]

if N in squares:
    print(1)
else:
    print(0)

"""
4
>
1
"""