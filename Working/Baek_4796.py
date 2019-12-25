"""
    @ Baek 4796
    @ Prob. https://www.acmicpc.net/problem/4796
      Ref. https://kwanghyuk.tistory.com/123
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 24
    @ End day: 19. 12. 24
"""

def solution(stayDay, partDay, totalDay):
    answer = 0
    quotient = totalDay // partDay
    answer = quotient * stayDay

    option = stayDay if (totalDay % partDay > stayDay) else totalDay % partDay
    answer += option
    return answer

arr = []
N = 0
while True:
    arr.append(list(map(int, input().split())))
    if arr[N][0] == 0:
        for i in range(N):
            stayDay, partDay, totalDay = arr[i]
            result = solution(stayDay, partDay, totalDay)
            print("Case " + str(i+1) + ": " + str(result) )
        break
    else:
        N += 1


"""
5 8 20
5 8 17
5 8 15
0 0 0
"""

