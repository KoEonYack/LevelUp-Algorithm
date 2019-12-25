'''
    @ Baek 1700
    @ Prob. https://www.acmicpc.net/problem/1700
      Ref. https://donggod.tistory.com/89
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 24
    @ End day: 19. 12.
'''


def solution():
    answer = 0
    currentHoleState = []
    cache = []

    for i in range(N):
        if arr[i] in currentHoleState:      # 콘센트 구멍에 꽂힌 경우
            continue
        elif len(currentHoleState) < numHole: # 여유 자리가 있는 경우
            currentHoleState.append(arr[i])
        else:                         # 현재 꼽힌 것 중 가장 나중에 사용하는거 제거
            answer += 1
            longVal = 0
            for num in currentHoleState:


    return answer


numHole, N = map(int, input().split())
arr = list(map(int, input().split()))

print(solution())




"""
2 7
2 3 2 3 1 2 7
"""