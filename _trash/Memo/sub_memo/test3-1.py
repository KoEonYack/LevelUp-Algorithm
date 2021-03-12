
def checkParenthesis(stack):
    if :
        return False

    elif :
        return False


def solution(inputStr):
    answer = False
    stack = []

    for char in inputStr:

        # 여는 괄호
        if char is '[' or  char is '{' or  char is '(':
            stack.append(char)

        # 닫는 괄호
        elif char is ']':
            if stack[:-1] is '[':
                stack.remove(stack[:-1])
        elif char is '}':
            if stack[:-1] is '}':
                stack.remove(stack[:-1])
        elif char is ')':
            if stack[:-1] is ')':
                stack.remove(stack[:-1])

    if len(stack) is 0:
        answer = True

    return answer