"""
    @ Baek 14426. 접두사 찾기
    @ Prob. https://www.acmicpc.net/problem/14426
      Ref.
    @ Algo: Search - Hash 460ms
    @ Note. 앞 글자 Hash
    @ Start day: 20. 09. 21.
    @ End day: 20. 09. 21.
"""


from bisect import bisect

N, M = map(int, input().split())
D = sorted([input() for i in range(N)])

ans = 0
for i in range(M):
    s = input()
    k = bisect(D, s)

    if (k > 0 and D[k-1][:len(s)] == s) or \
       (k < N and D[k][:len(s)] == s):
        ans += 1

print(ans)