"""
    @ Baek 14426. 접두사 찾기
    @ Prob. https://www.acmicpc.net/problem/14426
      Ref.
    @ Algo:
        Search 972ms
        Sort   904ms
    @ Note.
    @ Start day: 20. 09. 21.
    @ End day: 20. 09. 21.
"""

from sys import stdin
input = stdin.readline


N, M = map(int, input().split())
S = sorted([stdin.readline().strip() for _ in range(N)])
P = sorted([stdin.readline().strip() for _ in range(M)])

ans = 0
for p in P:      # O(N)
    for s in S:  # O(M)
        if s.startswith(p):
            ans += 1
            break

print(ans)


"""
5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus
>
7
"""