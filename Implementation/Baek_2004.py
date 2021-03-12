"""
    @ Baek 2004 조합 0의 개수
    @ Prob. https://www.acmicpc.net/problem/2004
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26.
    @ End day: 20. 01. 26.
"""


def five_count(n):
    ans = 0
    while n != 0:
        n = n // 5
        ans += n
    return ans


def two_count(n):
    ans = 0
    while n != 0:
        n = n // 2
        ans += n
    return ans


N, M = map(int, input().split())

if M == 0:
    print(0)
else:
    print(min(two_count(N)-two_count(M)-two_count(N-M), five_count(N)-five_count(M)-five_count(N-M)))


"""
25 12
>
2
"""