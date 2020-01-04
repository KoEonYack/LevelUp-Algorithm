"""
    @ Baek 2751 (pypy3로 제출)
    @ Prob. https://www.acmicpc.net/problem/2751
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 01. 04
    @ End day:  20. 01. 04
"""

import sys

arr = [int(input()) for _ in range(int(input()))]
sys.stdout.write("\n".join(map(str, sorted(arr))))

"""
5
5
4
3
2
1
>>>

1
2
3
4
5
"""