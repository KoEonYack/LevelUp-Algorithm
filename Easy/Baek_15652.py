"""
    백준 15652번 N과 M (4)
    Prob https://www.acmicpc.net/problem/15652
    End Day : 2020. 1. 1
"""


from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]

for ele in list(combinations_with_replacement(arr, M)):
    for num in ele:
        print(num, end=" ")
    print(end="\n")


"""
4 4 

"""