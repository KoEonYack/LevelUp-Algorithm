"""
    @ Baek 1697. 숨바꼭질
    @ Prob. https://www.acmicpc.net/problem/1697
     Ref.
    @ Algo: BFS
    @ Start day: 20. 07. 04.
    @ End day: 20. 07. 04. [Not Solved]
    @ Note:
"""

from collections import deque


def BFS():
    while q:
        x = q.popleft()
        if x == K:
            return ch[x]
        for nx in [x*2, x-1, x+1]:
            if 0 <= nx < 100001 and not ch[nx]:
                ch[nx] = ch[x] + 1
                q.append(nx)


# 수빈이 위치, 동생 위치  --> 동생
N, K = map(int, input().split())
ch = [0] * 100001
q = deque()
q.append(N)
print(BFS())
# print(ch)


"""
5 17
>
4
"""