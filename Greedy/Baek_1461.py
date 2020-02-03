"""
    @ 1461. 도서관
    @ Prob. https://www.acmicpc.net/problem/1461
     Ref. https://github.com/foreverever/baekjoon/blob/master/baekjoon/%EB%8F%84%EC%84%9C%EA%B4%80(1461).cpp
    @ Algo: Greedy
    @ Start day: 20. 02. 02.
    @ End day: 20. 02. 02.
"""

from collections import deque

N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
maxVal = 0
if abs(books[0]) < abs(books[-1]):
    maxVal = abs(books[-1])
else:
    maxVal = abs(books[0])

ans = 0

pos_deQ = deque([])
neg_deQ = deque([])

for i in range(N):
    if books[i] > 0:
        pos_deQ.append(books[i])
    else:
        neg_deQ.append(-books[i])

while pos_deQ:
    val = pos_deQ.pop()
    ans += val * 2
    #print(val)
    for i in range(M-1):
        if len(pos_deQ) == 0:
            break
        pos_deQ.pop()

#print("-----------")
while neg_deQ:
    val = neg_deQ.popleft()
    ans += val * 2
    #print(val)
    for i in range(M-1):
        #print(neg_deQ)
        if len(neg_deQ) == 0:
            break
        neg_deQ.popleft()


print(abs(ans - maxVal))


"""
7 2
-37 2 -6 -39 -29 11 -28
>
131
----------------------------------
7 2
-39 -37 -29 -28 -6 2 11 
>
131
"""