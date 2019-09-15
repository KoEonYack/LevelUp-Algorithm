'''
    @ Codility -sample test
    @ Prob. https://app.codility.com/demo/take-sample-test/
    @ Start Day: 2019. 09. 15.
    @ End Day: 2019. 09. 15.
'''


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    B = [1] * (len(A) + 2)

    for i in range(len(A)):
        if A[i] < 0:
            continue
        elif A[i] == 0:
            continue
        elif A[i] > 0:
            B[A[i]] = 0

    print(B)
    for i in range(1, 1000000):
        if B[i] is not 0:
            print(i)
            break


solution([1, 2, 3])
