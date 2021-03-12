"""
    @ Baek 4949 균형잡힌 세상
    @ Prob. https://www.acmicpc.net/problem/4949
     Ref.
    @ Algo: 스택
    @ Start day: 20. 04. 16.
    @ End day: 20. 04. 16.
"""

import sys
from collections import deque

while True:
    q = deque()
    S = input()
    if S == ".": break

    check = True
    for ch in S:
        if ch == "(" or ch == "[":
            q.append(ch)
        elif ch == ")":
            if len(q) == 0 or q[-1] != "(":
                check = False
                break
            q.pop()
        elif ch == "]":
            if len(q) == 0 or q[-1] != "[":
                check = False
                break
            q.pop()
    if len(q) > 0: check = False
    if check is True:
        print("yes")
    else:
        print("no")

"""
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
yes
yes
no
no
no
yes
yes
"""
