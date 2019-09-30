'''
    @ 5. 나이 계산
    @ Idea.
    @ TestCase: 780316-2376152
                42 W

                061102-3575393
                14 M
    @ Start day: 19. 09. 30
    @ End day: 19. 09. 30
'''

#personalNum = input()
str = "780316-2376152"
result = ""
Year = ""
personalNumArr = str.split("-")

if int(personalNumArr[1][0]) is 1 or int(personalNumArr[1][0]) is 2:
    Year = int(personalNumArr[0][0:2]) + 1900

elif int(personalNumArr[1][0]) is 3 or int(personalNumArr[1][0]) is 4:
    Year = int(personalNumArr[0][0:2]) + 2000

if int(personalNumArr[1][0]) % 2 == 0:
    result = "W"
else:
    result = "M"

print(2019 - Year + 1, result)