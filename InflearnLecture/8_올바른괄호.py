'''
    @ 8. 올바른 괄호
    @ Idea. 문자열 다루기
    @ TestCase: (()(()))(()
                No


    @ Start day: 19. 09. 30
    @ End day: 19. 09. 30
'''

cnt = 0
str = "()()(()())"

for a in str:
    if a == '(':
        cnt += 1
    elif a == ')':
        cnt -= 1
    if cnt < 0:
        break

if cnt == 0:
    print("Yes")
else:
    print("No")