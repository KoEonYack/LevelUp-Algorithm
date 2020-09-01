"""
    @ Baek 9935 문자열 폭발 [Fail]
    @ Prob. https://www.acmicpc.net/problem/9935
      Ref.
    @ Algo: 스택
    @ Start day: 20. 08. 31.
    @ End day: 20. 08. 31.
"""

# S = "mirkovC4nizCC44"
# ban = "C4"
# S = "12ab112ab2ab"
# ban = "12ab"
# S = "aaaa"
# ban = "a"

S = input()
ban = input()
stack = [""] * 1000010

ptr = 0
for i, s in enumerate(S):
    stack[ptr] = s
    if stack[ptr] == ban[-1]:
        if "".join(stack[ptr-len(ban)+1:ptr+1]) == ban:
            for j in range(ptr-len(ban)+1, ptr+1):
                stack[j] = ""
            ptr -= len(ban)
    ptr += 1

if "".join(stack) == "":
    print("FRULA")
else:
    print("".join(stack))
    

    
"""
mirkovC4nizCC44
C4
>
mirkovniz

-----------------------

12ab112ab2ab
12ab
>
FRULA
"""


