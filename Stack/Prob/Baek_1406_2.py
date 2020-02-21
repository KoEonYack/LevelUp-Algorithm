"""
    @ 1406 에디터
    @ Prob. https://www.acmicpc.net/problem/1406
     Ref.
    @ Algo: Stack
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""

from collections import deque
import sys

#input = sys.stdin.readline
#print = sys.stdout.write

#leftQ = deque(list(input()))
leftQ = [input()]
N = int(input())
#rightQ = deque([])


rightQ = []

for i in range(N):
    command = list(map(str, input().split()))
    if command[0] == "L":
        if len(leftQ) != 0:
            rightQ.append(leftQ.pop())

    elif command[0] == "D":
        if len(rightQ) != 0:
            leftQ.append(rightQ.pop())

    elif command[0] == "B":
        if len(leftQ) != 0:
            leftQ.pop()

    elif command[0] == "P":
        leftQ.append(command[1])


#while rightQ:
#    leftQ.append(rightQ.pop())

#for a in leftQ:
#    print(a, end="")

print(''.join(leftQ+rightQ[::-1]))
#res = ""
#for a in rightQ:
#    res = a + res

#print(res, end="")


"""
abcd
3
P x
L
P y
>
abcdyx
-----------------------
abc
9
L
L
L
L
L
P x
L
B
P y
>
yxabc
-----------------------
dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z
>
yxz
"""