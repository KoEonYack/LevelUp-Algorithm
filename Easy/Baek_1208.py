"""
    @ Baek 1208 부분수열의 합 2 ??
    @ Prob. https://www.acmicpc.net/problem/1208
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

from itertools import combinations

N, ans = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(1, N+1):
    for ele in list(combinations(arr, i)):
        if sum(ele) == ans:
            count += 1

print(count)

"""
5 0
-7 -3 -2 5 8
>
1
"""