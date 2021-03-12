"""
    @ Baek 1158 요세푸스 문제
    @ Prob. https://www.acmicpc.net/problem/1158
      Ref.
      Ref Prob.
    @ Algo: 구현(큐)
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""


from collections import deque

# N:사람 수 K: 죽일 사람의 위치
N, K = map(int, input().split())
Q = deque([i for i in range(1, N+1)])
cnt = 0
print("<", end="")
while Q:
    cnt += 1
    if cnt % K == 0:
        if len(Q) == 1: print(Q.popleft(), end="")
        else: print(Q.popleft(), end=", ")
    else:
        Q.append(Q.popleft())
print(">", end="")

"""
7 3
>
<3, 6, 2, 7, 5, 1, 4>
"""