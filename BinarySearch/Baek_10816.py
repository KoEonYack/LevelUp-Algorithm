"""
    @ Baek 10816, 숫자카드2
    @ Prob. https://www.acmicpc.net/problem/10816
      Ref. https://codedrive.tistory.com/184
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 19. 12. 30
    @ End day: 19. 12. 30
"""

import bisect

N = int(input())
OwingCardArr = list(map(int, input().split()))

M = int(input())
SearchCardArr = list(map(int, input().split()))
OwingCardArr.sort()

for i in range(M):
    idx1 = bisect.bisect_left(OwingCardArr, SearchCardArr[i])
    if idx1 < N and OwingCardArr[idx1] == SearchCardArr[i]:
        idx2 = bisect.bisect_left(OwingCardArr, SearchCardArr[i]+1)
        print(idx2-idx1, end=" ")
    else:
        print(0, end=" ")

"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

>>
3 0 0 1 2 0 0 2
"""