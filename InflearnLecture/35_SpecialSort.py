'''
    @ 35. Special Sort
    @ Idea. 정렬
    @ TestCase:
        Input: 8
               1 2 3 -3 -2 5 6 -6
        Output: -3 -2 -6 1 2 3 5 6
    @ Start day: 19. 09. 28
    @ End day: 19. 09. 28
'''

'''
# 방법 1
def solution(Arr):
    NegArr = []
    ArrNum = len(Arr)
    i=0
    while i < ArrNum:
        print(i, ArrNum, Arr, NegArr)
        if Arr[i] < 0:
            NegArr.append(Arr[i])
            Arr.remove(Arr[i])
            ArrNum = len(Arr)
            i = 0
            continue
        i += 1

    Arr.sort()
    print(NegArr + Arr)
'''

# 방법 2
def solution(Arr):
    for i in range(N-1): # 0 ~ n-1
        for j in range(N-i-1):
            if Arr[j] > 0 and Arr[j+1]<0:
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]

    print(Arr)


N = int(input("Input N.>"))
Arr = list(map(int, input().split()))
solution(Arr)

