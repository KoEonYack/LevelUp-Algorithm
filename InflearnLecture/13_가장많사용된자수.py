'''
    @ 13. 가장 많이 사용된 자릿수
    @ Idea. 자릿수
    @ TestCase: 1230565625
                5
    @ Start day: 19. 10. 07
    @ End day: 19. 10. 07
'''


str = "112233"
countArr = [0] * 10

for a in str:
    countArr[int(a)] += 1

print(countArr.index(max(countArr)))