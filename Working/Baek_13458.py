'''
    @ Baek 13458
    @ Prob. https://www.acmicpc.net/problem/13458
      Ref.
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 23.
    @ End day: 19. 12. 23.
'''


def solution():
    answer = 0

    # Master 시행
    for i in range(N):
        if arr[i] > 0:
            arr[i] -= Master
            answer += 1

        if arr[i] > 0:
            answer += int(arr[i]/Sub)

            if arr[i] % Sub != 0:
                answer += 1

    return answer


N = int(input())
arr = list(map(int, input().split()))
Master, Sub = map(int, input().split())
print(solution())

"""
5
10 9 10 9 10
7 2
"""