"""
    백준 15650번 N과 M (2)
    Prob https://www.acmicpc.net/problem/15650
    End Day : 2020. 1. 1
"""

from itertools import combinations

N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]

for ele in list(combinations(arr, M)):
    for num in ele:
        print(num, end=" ")
    print(end="\n")


"""
4 4 

"""