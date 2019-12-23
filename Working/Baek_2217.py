'''
    @ Prob. https://www.acmicpc.net/problem/2217
    @ Baek 2217
      Ref. https://penglog.tistory.com/113
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 23.
    @ End day:
'''


def solution():
    answer = 0
    arr.sort(reverse=True)
    for i in range(N):
        arr[i] = arr[i] * (i + 1)

    #print(arr)
    return max(arr)


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(solution())

'''
2
10
15
'''