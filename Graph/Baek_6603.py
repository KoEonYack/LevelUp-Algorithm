"""
    @ 6603. 로또
    @ Prob. https://www.acmicpc.net/problem/6603
     Ref.
    @ Algo: DFS
    @ Start day: 19. 12. 27.
    @ End day: 19. 12. 27.
"""

import itertools


inputArr = []
while True:
    inputArr = list(map(int, input().split()))
    inputArr.pop(0)
    if len(inputArr) == 0:
        break

    combArr = list(itertools.combinations(inputArr, 6))

    for arr in combArr:
        for num in arr:
            print(num, end=" ")
        print()
    print()



"""
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

"""