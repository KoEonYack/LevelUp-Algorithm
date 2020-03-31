"""
    @ Baek 1021 회전하는 큐
    @ Prob. https://www.acmicpc.net/problem/1021
      Ref.
      Ref Prob.
    @ Algo: 시뮬레이션
    @ Start day: 20. 03. 31.
    @ End day: 20. 03. 31.
"""

from collections import deque

N, M = map(int, input().split())
q = deque([i for i in range(1, N+1)])
find_arr = list(map(int, input().split()))
cnt = 0
while find_arr:
    pos = q.index(find_arr[0])
    size = len(q)
    left = pos
    right = size - pos - 1
    front = q.popleft()
    q.appendleft(front)
    print(front, find_arr[0], q)
    if front == find_arr[0]:
        find_arr.remove(front)
        q.popleft()
    elif left > right: # 우측으로 돌리자
        q.rotate(-1)
        cnt += 1
    else:
        q.rotate(1)
        cnt += 1

print(cnt)
        

"""
10 3
1 2 3
>
0
-------------
10 3
2 9 5
>
8
-------------
32 6
27 16 30 11 6 23
>
59
-------------


"""