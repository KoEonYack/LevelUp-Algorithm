'''
    @ 15. 소수의 갯수(1초)
    @ Idea. 소수 이론
        1 * 36 = 36
        2 * 18
        3 * 12
        4 * 9
        6 * 6
    @ TestCase:
        input  20
        output 8
    @ Start day: 19. 10. 07
    @ End day: 19. 10. 07
'''

N = int(input(""))
cnt = 0


for i in range(2, N+1): # 2 ~ N
    flag = 1

    j = 2
    while j*j <= i:
        if i % j is 0:
            flag = 0
            break
        j += 1

    if flag is 1:
        cnt += 1

print(cnt)
