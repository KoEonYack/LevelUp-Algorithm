'''
    @ 22. 온도의 최댓값
    @ Idea.
    @ TestCase:
        input.
                10 2
                3 -2 -4 -9 0 3 7 13 8 -3
        output.
                21
    @ Start day: 19. 10. 08
    @ End day: 19. 10. 08
'''

N, K = 10, 2
A = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
maxV = -9999999

for i in range(N-K+1):

    print(A[i:i+K:]) # 0 ~ 9
    if sum(A[i:i+K:]) > maxV :
        maxV = sum(A[i:i+K:])

print(maxV)
