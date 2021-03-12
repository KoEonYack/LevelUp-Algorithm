"""
    @ 10773 제로
    @ Prob. https://www.acmicpc.net/problem/10773
     Ref.
    @ Algo: Stack
    @ Start day: 20. 01. 26.
    @ End day: 20. 01. 26.
"""

stack = []
for i in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))

"""
10
1
3
5
4
0
0
7
0
0
6
>
7
"""