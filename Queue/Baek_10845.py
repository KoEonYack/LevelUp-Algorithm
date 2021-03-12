"""
    백준 10845번 큐
    Prob https://www.acmicpc.net/problem/10845
    End Day : 2020. 1. 1
"""

from sys import stdin

N = int(input())
qu = []

for _ in range(N):
    arr = stdin.readline().split()
    if arr[0] == "push":
        qu.append(arr[1])
    elif arr[0] == "pop":
        if qu: print(qu.pop(0))
        else: print(-1)
    elif arr[0] == "front":
        if qu: print(qu[0])
        else: print(-1)
    elif arr[0] == "back":
        if qu: print(qu[-1])
        else: print(-1)
    elif arr[0] == "size":
        print(len(qu))
    elif arr[0] == "empty":
        print(1-int(bool(qu)))
    else:
        pass

"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

>>>
1
2
2
0
1
2
-1
0
1
-1
0
3

"""