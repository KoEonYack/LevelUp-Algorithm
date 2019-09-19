'''
    @ Baek 1920
    @ Prob. https://www.acmicpc.net/problem/1920
      Ref.
    @ Algo: Sorting
    @ Start day: 19. 09. 19
    @ End day:
'''

def binSearch(n, target):
    start = 0
    end = n - 1

    while end - start >= 0:
        mid = int ( (start + end) / 2 )
        #print(inputArr[mid], target)
        if inputArr[mid] is target:
            return 1
        elif inputArr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


InputArrLen = int(input())
inputArr = list(map(int, input().split()))
inputArr.sort()
SearchArrLen = int(input())
searchArr = list(map(int, input().split()))



for i in range(SearchArrLen):
    print(binSearch(InputArrLen, searchArr[i]))
