'''
    @ 18. 층간소음
    @ Idea. 배열의 탐색

    @ TestCase:
        input.
                10 90
                23 17 120 34 112 136 123 23 25 113
        output. 3
    @ Start day: 19. 10. 07
    @ End day: 19. 10. 07
'''

Num, MaxVal = 10, 90
lst = [23, 17, 120, 34, 112, 136, 123, 23, 25, 113]
length = 0
candidateLength = []

for num in lst:

    if num < MaxVal:
        if length > 0:
            candidateLength.append(length)
        length = 0
    elif num > MaxVal:
        length += 1

if len(candidateLength) is 0:
    print(-1)
else:
    print(max(candidateLength))
