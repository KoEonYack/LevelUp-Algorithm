"""
19-N
"""


MINVAL = 99999999



def solution():
    min_move = MINVAL

    for top in range(1, 7):
        move = 0
        for i in range(len(A)):
            move += cost[A[i]][top]
        min_move = min(min_move, move)

    return min_move



N = int(input())
A = [int(input()) for _ in range(N)]

print(solution())

"""
7
0 1 2 3 4 5 6
0 0 1 1 1 1 2
0 1 0 1 1 2 1
0 1 1 0 2 1 1 
0 1 1 2 0 1 1
0 1 2 1 1 0 1
0 2 1 1 1 1 0
>


"""
