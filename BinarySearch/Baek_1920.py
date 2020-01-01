"""
    @ Baek 1920
    @ Prob. https://www.acmicpc.net/problem/1920
      Ref. https://wootool.tistory.com/114
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 19. 12. 30
    @ End day: 19. 12. 30
"""

def binarySearch(target):
    start = 0
    end = ArrNumLen - 1

    while start <= end:
        mid = (start + end) // 2
        if ArrNumArr[mid] == target:
            print(1)
            return
        elif ArrNumArr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    print(0)
    return


ArrNumLen = int(input())
ArrNumArr = list(map(int, input().split()))
SearchNumLen = int(input())
SearchNumArr = list(map(int, input().split()))
ArrNumArr.sort()

for searchNum in SearchNumArr:
    binarySearch(searchNum)

"""
5
4 1 5 2 3
5
1 3 7 9 5

>>
1
1
0
0
1
"""