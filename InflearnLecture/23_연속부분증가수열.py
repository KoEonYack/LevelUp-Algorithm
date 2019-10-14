'''
    @ 23. 연속 부분 증가수열
    @ Idea.
    @ TestCase:
        input.
                9
                5 7 3 3 12 12 13 10 11
        output.
                5
    @ Start day: 19. 10. 08
    @ End day: 19. 10. 08
'''

A = [5, 7, 3, 3, 12, 12, 13, 10, 11]
cnt = 0
maxV = 1
pre = A[0]
for i in range(1, len(A)):
    now = A[i]
    if now >= pre:
        cnt += 1
        if cnt > maxV:
            maxV = cnt
    else:
        cnt = 1
    pre = A[i]

print(maxV)