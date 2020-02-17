"""
    @ 1406 에디터
    @ Prob. https://www.acmicpc.net/problem/1406
     Ref.
    @ Algo: Stack
    @ Start day: 20. 02. 16.
    @ End day: 20. 02. 16.
"""

input_str = input()
arr = list(input_str)
cord = len(arr) -1

for i in range(int(input())):
    command = list(map(str, input().split()))
    if command[0] == "P":
        arr.insert(cord, command[1]) # 인덱스, 값
        cord += 1
    elif command[0] == "L":
        if cord == 0:
            continue
        cord -= 1
    elif command[0] == "D":
        if cord == len(arr)-1:
            continue
        cord += 1
    elif command[0] == "B":
        if cord == 0:
            continue
        print("pop", cord)
        print(arr)
        arr.pop(cord)
        cord -= 1

print(arr)

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