'''
    @ 17. 선생님 퀴즈
    @ Idea. 누적합

    @ TestCase:
        input.
            3
            10 55
            20 350
            100 5050
        output.
            YES
            NO
            YES
    @ Start day: 19. 10. 07
    @ End day: 19. 10. 07
'''

def culSum(x):
    sum = 0
    for i in range(1, x+1):
        sum += i
    return sum

lst = [[10, 55], [20, 350], [100, 5050]]
for a in lst:
    if a[1] == culSum(a[0]):
        print("YES")
    else:
        print("NO")
