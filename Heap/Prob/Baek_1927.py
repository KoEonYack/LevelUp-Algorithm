"""
    @ 1927. 최소 힙
    @ Prob. https://www.acmicpc.net/problem/1927
      가장 작은 값을 출력
     Ref.
    @ Algo: Heap
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

import heapq, sys

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)


"""
9
0
12345678
1
2
0
0
0
0
32
>
0
1
2
12345678
0
"""