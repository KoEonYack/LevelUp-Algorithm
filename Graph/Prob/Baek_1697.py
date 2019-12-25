'''
    @ 1697. 숨바꼭질
    @ Prob. https://www.acmicpc.net/problem/1697
     Ref. https://jun-itworld.tistory.com/19?category=778547
    @ Algo: BFS
    @ Start day: 19. 09. 03
    @ End day:
    @ Note:
리스트(List)를 큐로 사용하면 절대 안됩니다. 큐는 반드시 collections.deque를 써야 합니다.
queue.Queue는 멀티스레딩을 위해 만들어진 큐이고 매우 느립니다.
'''


from collections import deque


def bfs():
    q = deque()
    q.append(N)

    while q:
        step = q.popleft()
        if step == M:
            return arriveTime[step]

        for nextStep in (step - 1, step + 1, step * 2):
            if 0 <= nextStep < MAX and not arriveTime[nextStep]:
                arriveTime[nextStep] = arriveTime[step] + 1
                q.append(nextStep)


#N : 수빈이가 있는 위치, M: 동생이 있는 위치
MAX = 100001
N, M = map(int, input().split())
arriveTime = [0] * MAX
print(bfs())

"""
5 17
> 4
"""

"""
if 0 <= step - 1 < MAX and arriveTime[step-1] is 0:
    q.append(step-1)
    arriveTime[step-1] = arriveTime[step] + 1
if 0 <= step + 1 < MAX and arriveTime[step+1] is 0:
    q.append(step+1)
    arriveTime[step+1] = arriveTime[step] + 1
if 0 <= step * 2 <= MAX and arriveTime[step*2] is 0:
    q.append(step*2)
    arriveTime[step*2] = arriveTime[step] + 1
"""