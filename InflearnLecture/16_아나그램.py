'''
    @ 17. 아나그램
    @ Idea. 문자의 아스키코드 값을 배열의 인덱스로 접근.
            A(65) ~ Z(65+27)
            a(97) ~ z(97+27)
    @ TestCase:
    @ Start day: 19. 09. 22
    @ End day: 19. 09. 22
'''

checkA = [0] * 60
checkB = [0] * 60

aStr = input("문자열(1)을 입력해주세요")
for a in aStr:
    if 65 <= ord(a) and ord(a) <= 90:
        checkA[ord(a) - 65] += 1
    else:
        checkA[ord(a) - 70] += 1

bStr = input("문자열(2)을 입력해주세요")
for a in aStr:
    if 65 <= ord(a) and ord(a) <= 90:
        checkB[ord(a) - 65] += 1
    else:
        checkB[ord(a) - 70] += 1

for i in range(len(checkA)):
    if checkA[i] != checkB[i]:
        print(i)
        print("Not Anagram")
        break

