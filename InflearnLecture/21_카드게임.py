'''
    @ 21. 카드게임
    @ Idea.
    @ TestCase:
        input.
                4 5 6 7 0 1 2 3 9 8
                1 2 3 4 5 6 7 8 9 0
        output.
                Win A
    @ Start day: 19. 10. 08
    @ End day: 19. 10. 08
'''

A = [4, 5, 6, 7, 0, 1, 2, 3, 9, 8]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
N = len(A)
A_score = 0
B_score = 0
lastWinner = ""
for i in range(N):
    if A[i] > B[i]:
        A_score += 3
        lastWinner = "A"
    elif B[i] > A[i]:
        B_score += 3
        lastWinner = "B"
    elif A[i] == B[i]:
        A_score += 1
        B_score += 1

if A_score > B_score:
    print("Win A")
elif B_score > A_score:
    print("Win B")
elif A_score == B_score:
    if lastWinner == "":
        print("동점")
    elif lastWinner == "A":
        print("Win A")
    elif lastWinner == "B":
        print("Win B")
