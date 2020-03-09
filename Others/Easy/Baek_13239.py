"""
    @ 백준 13239 Combinations
    @ https://www.acmicpc.net/problem/13239
    @ End Day : 2020. 03. 09.
"""

from math import factorial
mod = 1000000007
for _ in range(int(input())):
    N, K = map(int, input().split())
    print((factorial(N) // (factorial(N-K) * factorial(K))) % mod)


"""
6
5 0
5 1
5 2
5 3
5 4
5 5
>
1
5
10
10
5
1
-----------------
3
123 54
7 4
20 10
>

"""

