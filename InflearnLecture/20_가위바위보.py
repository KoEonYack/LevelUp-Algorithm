'''
    @ 20. 가위 바위 보
    @ Idea. 전략 세우기
            A가 이기는 경우만 생각하면 나머지는 B가 이기는 경우가 될 것이다.
    @ TestCase:
        input.
                2 3 3 1 3
                1 1 2 2 3
        output.
                A
                B
                A
                B
                D
    @ Start day: 19. 10. 08
    @ End day: 19. 10. 08
'''

N = 5
A = [2, 3, 3, 1, 3]
B = [1, 1, 2, 2, 3]

for i in range(N):
    if A[i] is B[i]: # 비기는 경우
        print("D")
    elif A[i] == 1 and B[i] == 3: # A 가위(1) - B 보(3)
        print("A")
    elif A[i] == 2 and B[i] == 1: # A 바위(2) B 가위(1)
        print("A")
    elif A[i] == 3 and B[i] == 2: # A 보(3)  B 바위(2)
        print("A")
    else:                       # A가 이기지 않는 나머지의 경우
        print("B")