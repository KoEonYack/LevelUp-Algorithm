"""
    @ Baek 1806. 부분합
    @ Prob. https://www.acmicpc.net/problem/1806
     Ref.   https://suri78.tistory.com/165
    @ Algo: DP
    @ Start day: 20. 08. 29.
    @ End day: 20. 08. 29.
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

res_step = sys.maxsize
for i in range(1, N+1):
    val = 0
    step = 0
    for j in range(i, N+1):
        val += arr[j]
        step += 1
        if val >= M:
            res_step = min(res_step, step)
            break

if res_step == sys.maxsize:
    print(0)
else:
    print(res_step)

"""
10 15
5 1 3 5 10 7 4 9 2 8
>
3
"""