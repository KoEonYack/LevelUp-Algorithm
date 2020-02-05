"""
    @ 1783. 병든 나이트
    @ Prob. https://www.acmicpc.net/problem/1783
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 05.
    @ End day: 20. 02. 05.
"""

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, int((M+1)/2)))
elif N >= 3:
    if M <= 6:
        print(min(4, M))
    else:
        print(M-2)
