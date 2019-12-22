'''
    @ Baek 1931
    @ Prob. https://www.acmicpc.net/problem/1931
      Ref. https://suri78.tistory.com/26
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 22
    @ End day: 19. 12.
'''


def solution(InputArr):
    answer = 0
    endTime = 0
    for i in range(len(InputArr)):
        if endTime <= InputArr[i][0]:
            endTime = InputArr[i][1]
            answer += 1
    return answer


N = int(input())
InputArr = []

for i in range(N):
    A, B = map(int, input().split())
    InputArr.append([A, B])

InputArr.sort(key=lambda x: (x[1], x[0]))
print(solution(InputArr))

'''
2
2 2
1 2
2 가 나와야 하나 1이 나옴
'''