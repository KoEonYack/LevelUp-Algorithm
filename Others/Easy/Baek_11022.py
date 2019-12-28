    """
        백준 11022 A+B - 8
        End Day : 2019. 12. 28
    """

    N = int(input())

    for i in range(N):
        A, B = map(int, input().split())
        print("Case #" + str(i+1) + ": " + str(A) + " + " + str(B) + " =", A + B)


    """
    5
    1 1
    2 3
    3 4
    9 8
    5 2
    
    >
    Case #1: 1 + 1 = 2
    Case #2: 2 + 3 = 5
    Case #3: 3 + 4 = 7
    Case #4: 9 + 8 = 17
    Case #5: 5 + 2 = 7
    
    """