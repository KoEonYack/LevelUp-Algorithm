"""
    @ Baek 5430. AC
    @ Prob. https://www.acmicpc.net/problem/5430
     Ref.
    @ Algo: Implement
    @ Start day: 20. 06. 30.
    @ End day: 20. 06. 30.
"""

from collections import deque

T = int(input())
for _ in range(T):
    cmds = input()

    L = int(input())
    elements = deque(input()[1:-1].split(","))
    isReversed = False
    # print(elements, type(elements))

    flag = False
    for cmd in cmds:
        if cmd == "R":
            isReversed = False if isReversed else True
            # if isReversed:
            #     isReversed = False
            # else:
            #     isReversed = True
        elif cmd == "D":
            if L == 0:
                flag = True
                break
            elif isReversed is True:
                elements.pop()
                L -= 1
                # print("DEBUG1", elements)
            elif isReversed is False:
                elements.popleft()
                L -=1
                # print("DEBUG2", elements)


    if flag is True:
        print("error")
    else:
        if isReversed is True:
            elements.reverse()
            print("[", end="")
            print(",".join(list(elements)), end="")
            print("]")
        elif isReversed is False:
            print("[", end="")
            print(",".join(list(elements)), end='')
            print("]")
    flag = False


"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
>
[2,1]
error
[1,2,3,5,8]
error

1
RRD
6
[1,1,2,3,5,8]
"""