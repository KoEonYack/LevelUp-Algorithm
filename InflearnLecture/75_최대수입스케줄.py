"""
    @ 75. 최대 수입 스케줄
    @ Idea. 우선순위 큐
    @ Start day: 20. 01. 21.
    @ End day: 20. 01. 21.
"""

import heapq


N = int(input())
arr = []
pQ = []

max = 0
for i in range(N):
    inputArr = list(map(int, input().split()))
    arr.append(inputArr)
    if inputArr[1] > max: # 최고 높은 날짜 선택
        max = inputArr[1]

arr.sort(key=lambda x:x[1], reverse=True)
res = 0

j = 0
for i in range(max, 0, -1): # 최고날 부터 1
    while True:
        if j == N:
            break
        if arr[j][1] < i: # 탐색 날보다 작은 날은 취소
            break
        heapq.heappush(pQ, arr[j][0]*-1)
        j += 1

    if len(pQ) != 0:
        tmp = heapq.heappop(pQ)
        res += tmp * -1
        #print(tmp * -1)

print(res)

"""
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
>
185
---------------------------------
6
50 2
20 1
40 2
60 3
30 3
30 1
>
150
"""