'''
    @ 25. 석차 구하기
    @ Idea. 부르트포스
    @ TestCase:
        input.
                5
                90 85 92 95 90
        output.
                3 5 2 1 3
    @ Start day: 19. 10. 08
    @ End day: 19. 10. 08
'''

N = 5
A = [90, 85, 92, 95, 90]
B = [1] * 5

for i in range(len(A)):
    for j in range(len(A)):
        if A[i] > A[j]:
            B[j] += 1

print(B)

