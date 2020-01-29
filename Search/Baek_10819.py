"""
    @ Baek 10819 차이를 최대로
    @ Prob. https://www.acmicpc.net/problem/10819
      Ref.
      Ref Prob.
    @ Algo: Brute-force
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

import sys
from itertools import permutations


def abs_sum(per_list):
    div_sum = 0
    for i in range(len(per_list)-1):
        div_sum = div_sum + abs(per_list[i] - per_list[i+1])
    return div_sum


ans = -sys.maxsize
N = int(input())
per_list = permutations(list(map(int, input().split())))
for num_list in per_list:
    ans = max(ans, abs_sum(num_list))

print(ans)

"""
6
20 1 15 8 4 10

5
1 2 3 4 5
>
62
"""