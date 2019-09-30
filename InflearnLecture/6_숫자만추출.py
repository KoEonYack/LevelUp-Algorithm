'''
    @ 6. 숫자만 추출
    @ Idea.
    @ TestCase: g0en2Ts8eSoft
                28 6

    @ Start day: 19. 09. 22
    @ End day: 19. 09. 22
'''

inputStr = input("검사 문자를 입력해 주세요.")
result = ""
cnt = 0

for a in inputStr:
    if a.isdigit():
        result += a

for i in range(1, int(result)+1):
    if int(result) % i is 0:
        cnt += 1

print(int(result))
print(cnt)