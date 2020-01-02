"""
    백준 15654번 N과 M (5)
    Prob https://www.acmicpc.net/problem/15654
    End Day : 2020. 1. 1
"""

from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list)

for numbers in list(permutations(N_list, M)):
    for num in numbers:
        print(num, end=' ')
    print()

"""
4 2
9 8 7 1

>>
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
"""