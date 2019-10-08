'''
    @ 23. 연속 부분 증가수열 ?
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
culSum = 0

for i in range(len(A)-1):
    if A[i] < A[i+1]:
        cumSum = cumSum + A[i]