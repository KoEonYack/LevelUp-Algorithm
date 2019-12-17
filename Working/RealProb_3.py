'''

    햄버거 문제 - 알바를 고용

'''

def solution(str):
    stack = []

    for char in str:
        if char == '[':
            if ('{' in stack) or ('(' in stack or '{' in stack or '[' in stack):
                print(str + "\t No")
                return
            else:
                stack.append("[")
        elif char == '{':
            if '(' in stack or '{' in stack:
                print(str + "\t No")
                return
            else:
                stack.append("{")
        elif char == '(' :
            if '(' in stack:
                print(str + "\t No")
                return
            else:
                stack.append('(')

        elif  (char == '}' and '(' not in stack) or (char == ')') or (char == ']' and '{' not in stack and '(' not in stack):
            if len(stack) is 0:
                print(str + "\t No")
                return
            else:
                stack.remove(stack[-1])

    if len(stack) == 0:
        print(str + "\t Yes")
        return
    print(str + "\t No")



'''
solution("[()]")
solution("(())")
solution("[({})]")
solution("[()")
solution("{{}}")
solution("[[]]")
solution("[{]}")
solution("[{[]}]")
'''
solution("[())]")
solution("{(})")
