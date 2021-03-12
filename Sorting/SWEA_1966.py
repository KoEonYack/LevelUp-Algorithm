'''
    @ SWEA-1966 숫자를 정렬하자.
    @ Prob. https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq&categoryId=AV5PrmyKAWEDFAUq&categoryType=CODE&&&
      Ref. None
    @ Algo: Sorting
    @ Start day: 19. 09. 06
    @ End day: 19. 09. 06
'''

TestSetNum = int(input())
while TestSetNum:
    TestSetNum -= 1
    elementsNum = int(input())

    for i in range(1, elementsNum+1):
        arrStr = input()
        testArr = list(map(int, arrStr.split()))
        testArr.sort()
        testArr = list(map(str, testArr))
        testArr = " ".join(testArr)
        print("#{0} {1}".format(i, testArr))
