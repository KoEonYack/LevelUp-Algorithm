'''
    @ 6. 숫자만 추출
    @ Idea.
    @ TestCase:
    @ Start day: 19. 09. 22
    @ End day: 19. 09. 22
'''

inputStr = input("검사 문자를 입력해 주세요.")
result = ""

for a in inputStr:
    if a.isdigit():
        result += a

print(int(result))