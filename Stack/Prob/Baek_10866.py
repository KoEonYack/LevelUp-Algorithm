"""
    @ 10866 덱
    @ Prob. https://www.acmicpc.net/problem/10866
     Ref.
    @ Algo: Deque
    @ Start day: 20. 01. 28.
    @ End day: 20. 01. 28.
"""

from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

def isEmpty():
    if len(deq) == 0:
        return True
    else:
        return False


deq = deque([])
for i in range(int(input())):
    commandArr = list(map(str, input().split()))

    if commandArr[0] == "push_front":
        deq.appendleft(commandArr[1])

    elif commandArr[0] == "push_back":
        deq.append(commandArr[1])

    elif commandArr[0] == "pop_front":
        if isEmpty():
            print("-1")
        else:
            print(deq.popleft())
        print("\n")

    elif commandArr[0] == "pop_back":
        if isEmpty():
            print("-1")
        else:
            print(deq.pop())
        print("\n")

    elif commandArr[0] == "size":
        print(str(len(deq)))
        print("\n")

    elif commandArr[0] == "empty":
        if isEmpty():
            print("1")
        else:
            print("0")
        print("\n")

    elif commandArr[0] == "front":
        if isEmpty():
            print("-1")
        else:
            print(deq[0])
        print("\n")

    elif commandArr[0] == "back":
        if isEmpty():
            print("-1")
        else:
            print(deq[-1])
        print("\n")


"""
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
>
2
1
2
0
2
1
-1
0
1
-1
0
3

22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back
>
-1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20
"""