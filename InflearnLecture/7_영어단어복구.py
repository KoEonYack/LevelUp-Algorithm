'''
    @ 7. 영어단어 복구
    @ Idea. 문자열 다루기
    @ TestCase: bE    au T I fu   L

    @ Start day: 19. 09. 30
    @ End day: 19. 09. 30
'''

str = "bE    au T I fu   L"
str = str.lower()
res = ""
for a in str:
    if a.isspace():
        continue
    res += a
print(res)