"""
    @ Baek 10815, 숫자카드
    @ Prob. https://www.acmicpc.net/problem/10815
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 19. 12. 30
    @ End day: 19. 12. 30
"""


def BinarySearch(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if OwingCardArr[mid] == target:
            print(1, end=" ")
            return
        elif OwingCardArr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    print(0, end=" ")
    return


N = int(input())
OwingCardArr = list(map(int, input().split()))

M = int(input())
SearchCardArr = list(map(int, input().split()))
OwingCardArr.sort()
for num in SearchCardArr:
    BinarySearch(num)

"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10

>>
1 0 0 1 1 0 0 1
"""