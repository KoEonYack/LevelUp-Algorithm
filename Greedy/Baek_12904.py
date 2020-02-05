"""
    @ 12904. A와 B
    @ Prob. https://www.acmicpc.net/problem/12904
     Ref.
    @ Algo: Greedy
    @ Start day: 20. 02. 05.
    @ End day: 20. 02. 05.
"""

S = [i for i in input()]
T = [j for j in input()]

flag = False
while True:
    if len(S) == len(T):
        if "".join(S) == "".join(T):
            flag = True
        break
    c = T[len(T) - 1]
    T.pop()
    if c == 'B':
        T.reverse()

if flag is True:
    print(1)
else:
    print(0)



"""
B
ABBA
> 
1

AB
ABB
>
0
"""