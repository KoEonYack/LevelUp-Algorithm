'''
    @ 33. 3등의 성적은?
    @ Idea. 정렬
    @ TestCase:
        input 1: 7
                 80 96 75 82 96 92 100
        output 1: 92
    @ Start day: 19. 09. 28
    @ End day: 19. 09. 28
'''


def solution(Arr):
    cnt = 0

    for i in range(N-1): # 0 ~ n-1
        idx = i
        j = i + 1
        for j in range(j, N):
            if Arr[j] > Arr[idx]:
                idx = j
        Arr[idx], Arr[i] = Arr[i], Arr[idx]

    print(Arr)
    for i in range(1, N):
        if Arr[i-1] != Arr[i]:
            cnt += 1
        if cnt == 2:
            print(Arr[i])
            break


N = int(input("Input N"))
Arr = list(map(int, input().split()))
solution(Arr)
