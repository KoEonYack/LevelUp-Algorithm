"""
    @ Baek 11000 강의실 배정
    @ Error. 파이썬의 한계, 시간초과
    @ Prob. https://www.acmicpc.net/problem/11000
      Ref. https://hyp3rflow.tistory.com/3
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 23
    @ End day:
"""
from queue import PriorityQueue


def solution():
    pque = PriorityQueue()
    pque.put((-arr[0][1], arr[0][1]))
    #print(arr[0][1])
    for i in range(1, N):
        # print(pque.queue[-1][1], arr[i][0])
        if pque.queue[-1][1] <= arr[i][0]:
            pque.get()
            pque.put((-arr[i][1], arr[i][1]))
        else:
            pque.put((-arr[i][1], arr[i][1]))

    #print(pque)

    """
    for i in range(len(pque.queue)):
        print(pque.queue[i][1])
    """
    print(pque.qsize())
    return


N = int(input())
arr = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    arr.append([A, B])

arr.sort(key=lambda x: x[0])
#print(arr)
solution()


'''
3
1 3
3 5
2 4
'''