"""
    @ 11286. 절댓값 힙
    @ Prob. https://www.acmicpc.net/problem/11286
     Ref.
    @ Algo: Heap
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

import sys, heapq

heap = []
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))


"""
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
>>>>>>>
-1
1
0
-1
-1
1
1
-2
2
0
"""