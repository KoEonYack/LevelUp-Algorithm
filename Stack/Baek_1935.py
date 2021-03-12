"""
    @ 1935 후위 표기식2
    @ Prob. https://www.acmicpc.net/problem/1935
     Ref.
    @ Algo: Stack
    @ Start day: 20. 02. 23.
    @ End day: 20. 02. 23.
"""

from collections import deque

Stack = deque([])
N = int(input())
commands = list(input())
arr = [int(input()) for i in range(N)]

for t in commands:
    if 'A' <= t <= 'Z':
        Stack.append(arr[ord(t) - ord('A')])
    else:
        b = Stack.pop()
        a = Stack.pop()
        if t == '+':
            Stack.append(a+b)
        elif t == '-':
            Stack.append(a-b)
        elif t == '/':
            Stack.append(a/b)
        elif t == "*":
            Stack.append(a*b)

print("%.2f" % Stack[0])


"""
5
ABC*+DE/-
1
2
3
4
5
>
6.20
"""