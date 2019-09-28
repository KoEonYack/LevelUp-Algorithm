'''
    @ 36. 삽입정렬
    @ Idea. 정렬
    @ TestCase:
        input 1: 6
                 13 5 11 7 23 15
        Output: 5 6 7 9 10 11
    @ Start day: 19. 09. 28
    @ End day: 19. 09. 28
'''


def solution(Arr):
    for i in range(1, N): # 0 ~ n-1
        tmp = Arr[i]
        j = i - 1
        for k in range(j, 0, -1):
            if Arr[k] > tmp:
                Arr[k+1] = Arr[k]
            else:
                break
        Arr[j+1] = tmp
    print(Arr)


N = int(input("Input N.>"))
Arr = list(map(int, input().split()))
solution(Arr)
