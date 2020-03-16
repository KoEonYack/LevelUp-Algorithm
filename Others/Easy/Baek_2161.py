"""
    @ Baek 2161 카드1
    @ Prob. https://www.acmicpc.net/problem/2161
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""


# 우선, 제일 위에 있는 카드를 바닥에 버린다.
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

from collections import deque

N = int(input())
q = deque([i for i in range(1, N+1)])

while q:
    print(q.popleft(), end=" ")
    if len(q) != 0:
        q.append(q.popleft())

"""
7
>
1 3 5 7 4 2 6
"""