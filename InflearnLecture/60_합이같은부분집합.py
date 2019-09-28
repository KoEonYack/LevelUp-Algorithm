'''
    @ 60. 합이 같은 부분집합(아마존 인터뷰)
    @ Idea. DFS.
            부분 집합의 합을 별도의 list를 만드는 것이 아닌 전체 합에서 부분 집합 합을 빼는 방식으로 개선.
    @ TestCase:
    6
    1 3 5 6 7 10
    @ output: YES

    @ Start day: 19. 09. 26
    @ End day: 19. 09. 26
'''

import sys

def DFS(L, sum):
    if L is n + 1:
        if sum is total - sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+MapArr[L])
        DFS(L+1, sum)


ch = [0] * 11
MapArr = []
n = int(input())
MapArr = list(map(int, input().split()))
total = sum(MapArr)
print(MapArr)

DFS(1, 0)
