'''
    @ 48. 각 행의 평균과 가장 가까운 값
    @ Idea.
    @ TestCase:
        input:
                3 23 85 34 17 74 25 52 65
                10 7 39 42 88 52 14 72 63
                87 42 18 78 53 45 18 84 53
                34 28 64 85 12 16 75 36 55
                21 77 45 35 28 75 90 76 1
        output:
                42 34
                43 42
                53 53
                45 36
                50 45
    @ Start day: 19. 10. 14
    @ End day: 19. 10. 14
'''

InputArr = [[3, 23, 85, 34, 17, 74, 25, 52, 65],
            [10, 7, 39, 42, 88, 52, 14, 72, 63],
            [87, 42, 18, 78, 53, 45, 18, 84, 53],
            [34, 28, 64, 85, 12, 16, 75, 36, 55],
            [21, 77, 45, 35, 28, 75, 90, 76, 1]]

absArr = [0] * len(InputArr[0])

for arr in InputArr:

    avg = int(sum(arr) / len(arr))
    for i in range(len(arr)):
        absArr[i] = abs(avg-arr[i])

    print(avg, arr[absArr.index(min(absArr))])




