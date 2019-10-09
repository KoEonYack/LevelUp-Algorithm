'''
    @ 26. 마라톤
    @ Idea.
    @ TestCase:
        input.
                8
                2 8 10 7 1 9 4 15
        output.
                1 1 1 3 5 2 5 1
    @ Start day: 19. 10. 09
    @ End day: 19. 10. 09
'''


A = [2, 8, 10, 7, 1, 9, 4, 15]
result = 1
resultArr = []

for i in range(len(A)):
    result = 1
    for j in range(0, i): # 0 ~ i
        if A[i] < A[j]:
            result += 1
    resultArr.append(result)

print(resultArr)


