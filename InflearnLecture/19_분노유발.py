'''
    @ 19. 분노 유발자
    @ Idea. 배열의 탐색

    @ TestCase:
        input.
                10
                56 46 55 76 65 53 52 53 55 50
        output. 3
    @ Start day: 19. 10. 07
    @ End day: 19. 10. 07
'''


lst = [56, 46, 55, 76, 65, 53, 52, 53, 55, 50]
max = lst[len(lst) -1]
resultArr = []
result = 0
for i in range(len(lst)-1, -1, -1): # len(lst) ~ 0
    if lst[i] > max:
        result += 1
        max = lst[i]
        resultArr.append(lst[i])

print(result, end=" ")
print(resultArr, end=" ")
