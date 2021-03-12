"""
    @ 11279. 최소 힙
    @ Prob. https://www.acmicpc.net/problem/11279
      가장 큰 값을 출력
     Ref.
    @ Algo: Heap
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

import sys, heapq
heap = []

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline()) * -1
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, num)


"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
>
0
2
1
3
2
1
0
0
"""
