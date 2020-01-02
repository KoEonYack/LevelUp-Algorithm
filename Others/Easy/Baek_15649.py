"""
    백준 15649번 N과 M (1)
    Prob https://www.acmicpc.net/problem/15649
    End Day : 2020. 1. 1
"""


from itertools import permutations

N, M = map(int, input().split())
arr = [str(i+1) for i in range(N)]

for ele in list(permutations(arr, M)):
    for num in ele:
        print(num, end=" ")
    print(end="\n")


"""
4 4 

"""