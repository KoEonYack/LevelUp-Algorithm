"""
    @ Baek 9095 1, 2, 3 더하기
    @ Prob. https://www.acmicpc.net/problem/9095
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

N = int(input())
cache = [0] * 11
cache[1], cache[2], cache[3] = 1, 2, 4
for i in range(4, 11):
    cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
for i in range(N):
    print(cache[int(input())])

"""
3
4
7
10
>
7
44
274
"""