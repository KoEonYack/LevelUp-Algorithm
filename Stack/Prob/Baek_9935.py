"""
    @ Baek 9935 문자열 폭발 [Fail]
    @ Prob. https://www.acmicpc.net/problem/9935
      Ref.
    @ Algo: 스택
    @ Start day: 20. 08. 31.
    @ End day: 20. 08. 31.
"""


# S = list(input())
# boom = list(input()
stack = [""] * 30
S = "mirkovC4nizCC44"
boom = "C4"

str_ptr = 0
for i, s in enumerate(S):
    stack[str_ptr] = s
    
    # print("DEBUG-1/", stack[str_ptr], boom[-1], type(stack[str_ptr]), type(boom[-1]) , stack[-1] == boom[-1])
    
    
    if stack[str_ptr] == boom[-1]: 
        
        if "".join(stack[str_ptr-len(boom)+1:str_ptr+1]) == boom: 
            print("DEBUG-2/", "".join(stack[str_ptr-len(boom)+1:str_ptr+1]), boom, str_ptr)
            
            for i in range(str_ptr-len(boom)+1, str_ptr+1):
                stack[i] = ""
                print("=========")
                print(stack, i)
                print("=========")
            
            str_ptr = str_ptr - len(boom) - 1
    else:
        str_ptr += 1

    print(stack)
  



if stack[str_ptr] == boom[-1]:
    # print(stack[str_ptr+1:str_ptr+len(boom)+1], str_ptr)
    if "".join(stack[str_ptr+1:str_ptr+len(boom)+1]) == boom:
        for i in range(str_ptr+1, str_ptr+len(boom)+1):
            stack[i] = ""
    print(stack)


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