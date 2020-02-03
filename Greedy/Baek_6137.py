"""
    @ 6137. 문자열 생성 (Best cow line)
    @ Prob. https://www.acmicpc.net/problem/6137
     Ref. 노랭이 63p
    @ Algo: Greedy
    @ Start day: 20. 02. 03.
    @ End day: 20. 02. 03.
"""

from collections import deque

N = int(input())
S_arr = deque([])
T = ""
left_flag = False   
for _ in range(N):
    S_arr.append(input())

cnt = 0
for i in range(N):
    left_flag = False

    if S_arr[0] == S_arr[-1]:


    elif S_arr[0] >= S_arr[-1]:
        left_flag = False
        T += S_arr.pop()

    else:
        left_flag = True
        T += S_arr.popleft()

    if cnt % 80 == 0:
        T += "\n"

    cnt += 1


print(T)

"""
6
A
C
D
B
C
B
>
ABCBCD

6
A
B
C
D
E


6
G
F
A
B
F
G
>
GFBAFG
"""