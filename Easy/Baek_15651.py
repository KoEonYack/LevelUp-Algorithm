"""
    백준 15651번 N과 M (3)
    Prob https://www.acmicpc.net/problem/15651
    End Day : 2020. 1. 1
"""


from itertools import product

N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]

for ele in list(product(arr, repeat=M)):
    for num in ele:
        print(num, end=" ")
    print(end="\n")


"""
4 4 

"""