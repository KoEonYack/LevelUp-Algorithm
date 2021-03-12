"""
    @ Baek 1966 프린터 큐
    @ Prob. https://www.acmicpc.net/problem/1966
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

from collections import deque


def max_V(q):
    maxV = 0
    for num in q:
        if num[1] > maxV:
            maxV = num[1]
    return maxV


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    M_cost = arr[M]
    q = deque([])
    for i in range(N):
        q.append([i, arr[i]])

    count = 0
    while q:
        maxV = max_V(q)
        tmp = q.popleft()
        print(M_cost, maxV, M, tmp[0])
        if M_cost >= maxV and M == tmp[0]:
            print(count)
            break
        elif maxV == tmp[1]:
            continue
        else:
            count += 1
            q.append(tmp)


"""

1       # TestCase
1 2     # ArrNum NumOfDoc
1 2 3


1 
1 0 
5

1
4 2
1 2 3 4

1
6 0
1 1 9 1 1 1
>
1
2
5

"""