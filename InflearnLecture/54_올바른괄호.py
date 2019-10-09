'''
    @ 54. 올바른 괄호
    @ Idea. 스택, (를 만나면 PUSH, )를 만나면 POP
    @ TestCase:
        input: (()(()))(()
        output: NO

        input: ()()(()())
        output: YES
    @ Start day: 19. 10. 09
    @ End day: 19. 10. 09
'''
import sys

inputStr = "(()(()))(()"
inputArr = list(inputStr)
stack = []
for str in inputArr:
    if str == "(":
        stack.append("(")
    elif str == ")":
        if len(stack) == 0:
            print("NO")
            sys.exit(0)
        else:
            stack.pop()

if len(stack) == 0:
    print("YES")
else:
    print("NO")
print(stack)
