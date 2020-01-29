"""
    @ Baek 10972 다음 순열 ?
    @ Prob. https://www.acmicpc.net/problem/10972
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

from itertools import permutations
from sys import stdin
input = stdin.readline

N = int(input())
per_set_tuple = tuple(map(int, input().split()))
arr = [i for i in range(1, N+1)]
per_arr = permutations(arr, N)

flag = False
flag_last = False
for per_ele in per_arr:
    if per_ele == per_set_tuple:
        flag = True
        continue
    if flag is True:
        flag_last = True
        print(*per_ele)
        break

if flag_last is False:
    print(-1)

""" 
4
1 2 3 4
>
1 2 4 3

5
5 4 3 2 1
>
-1
"""