'''
    @ SWEA-1976 시각 덧셈
    @ Prob. https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PttaaAZIDFAUq
      Ref. None
    @ Algo:
    @ Start day: 19. 09. 09
    @ End day: 19. 09. 09
'''

NumOfTest = int(input())
itr = 1
arr = []

while itr <= NumOfTest:

    testCaseStr = input()
    arr = list(map(int, testCaseStr.split()))

    hour = arr[0] + arr[2]
    min = arr[1] + arr[3]

    if min > 60:
        min = min - 60
        hour = hour + 1

    if hour > 12:
        hour = hour - 12

    print("#{0}".format(itr))

    itr += 1