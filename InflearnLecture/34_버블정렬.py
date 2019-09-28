'''
    @ 34. 버블 정렬
    @ Idea. 버블 정렬
    @ TestCase:
        input 1: 7
                 80 96 75 82 96 92 100
        output 1: [75, 80, 82, 92, 96, 96, 100]
    @ Start day: 19. 09. 28
    @ End day: 19. 09. 28
'''


def solution(Arr):
    for i in range(N-1): # 0 ~ n-1
        for j in range(N-i-1):
            if Arr[j] > Arr[j+1]:
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]

    print(Arr)

N = int(input("Input N.>"))
Arr = list(map(int, input().split()))
solution(Arr)

