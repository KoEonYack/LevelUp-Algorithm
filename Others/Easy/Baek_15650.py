"""
    백준 15650번 N과 M (2)
    Prob https://www.acmicpc.net/problem/15650
    End Day : 2020. 1. 1
"""

from itertools import combinations

N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]

for ele in list(combinations(arr, M)):
    print(" ".join(ele))


"""
4 4 
1 2 3 4
---------
4 2
>
1 2
1 3
1 4
2 3
2 4
3 4
"""