"""
    @ 2529. 부등호
    @ Prob. https://www.acmicpc.net/problem/2529
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 03. 13.
    @ End day: 20. 03. 13.
"""

from collections import deque

N = int(input())
commands = input()
max_q = deque([i for i in range(9, 9-N, -1)])
min_q = deque([i for i in range(0, N)])


"""
2
< > 
------------
897
021
"""