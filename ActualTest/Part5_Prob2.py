"""
    스택 연습

"""

from collections import deque

par = ["[", "]", "{", "}", "(", ")"]

s = []
is_correct = True
inputStr = input()

for c in inputStr:
    if is_correct is False:
        break

    num_par_c = -1
    for i in range(6): # 괄호의 종류를 발견
        if c == par[i]:
            num_par_c = i
            break
    if num_par_c == -1: continue # 괄호가 아닌 문자가 경우

    if num_par_c % 2: # 여는 괄호가 나온 경우
        if len(s) != 0 and s[-1] == num_par_c - 1:
            s.pop()
        else:
            is_correct = False
    elif len(s) == 0 or s[-1] < num_par_c:
        s.append(num_par_c)
    else:
        is_correct = False

if len(s) == 0 and is_correct is True:
    print("true")
else:
    print("false")


"""
3+[(5+1)-1]
> true

3+([5+1])
> false

3+[{(5+1)-1}+3]
"""