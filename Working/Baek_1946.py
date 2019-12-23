"""
    @ Baek 1946 (pypy3 제출)
    @ Prob. https://www.acmicpc.net/problem/1946
      Ref. https://mygumi.tistory.com/120
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 23.
    @ End day:
"""


def solution():
    #print(arr)
    answer = 1
    tmp = arr[0][1]
    for i in range(1, N):
        #print(tmp , arr[i][1])
        if tmp >= arr[i][1]:
            tmp = arr[i][1]
            answer += 1

    return answer



iterNum = int(input())
for _ in range(iterNum):
    N = int(input())
    arr = []
    for _ in range(N):
        A, B = map(int, input().split())
        arr.append([A, B])
    arr.sort(key = lambda x : x[0])
    print(solution())