'''
    @ 32. N!의 표현법
    @ Idea. 선택 정렬. 가장 작은 원소를 찾으면 SWAP
    @ TestCase:
        input 1: 6
                 13 5 11 7 23 15
    @ Start day: 19. 09. 28
    @ End day: 19. 09. 28
'''


def solution(Arr):
    for i in range(N-1): # 0 ~ n-1
        idx = i
        j = i + 1
        for j in range(j, N):
            if Arr[j] < Arr[idx]:
                idx = j
        Arr[idx], Arr[i] = Arr[i], Arr[idx]

    print(Arr)

N = int(input("Input N"))
Arr = list(map(int, input().split()))
solution(Arr)
