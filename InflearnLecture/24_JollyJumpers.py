'''
    @ 24. Jolly Jumpers
    @ Idea.
    @ TestCase:
        input.
                5
                1 4 2 3 7
        output.
                YES
    @ Start day: 19. 10. 08
    @ End day: 19. 10. 08
'''

import sys
N = 5
A = [1, 4, 2, 3, 7]
check = [0] * (5)

for i in range(len(A)-1):
    if check[abs(A[i]-A[i+1])] == 0:
        check[abs(A[i]-A[i+1])] += 1
    else:
        print("Not jolly jumphers")
        sys.exit(0)
        break

print("Jolly Jumphers")