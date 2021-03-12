'''



'''

arr = []
def verify(H, M, ans):
    if H <= 23 and H >= 0 and M>= 0 and M<=59 and [H, M] not in arr:
        arr.append([H, M])
        return ans+1
    else:
        return ans


def solution(A, B, C, D):
    ans = 0
    h = 0
    m = 0

##### 1
    h = A * 10 + B
    m = C * 10 + D
    ans = verify(h, m, ans)

    m = D * 10 + C
    ans = verify(h, m, ans)
    #
    h = A * 10 + C
    m = B * 10 + D
    ans = verify(h, m, ans)

    m = D * 10 + B
    ans = verify(h, m, ans)
    #
    h = A * 10 + D
    m = B * 10 + C
    ans = verify(h, m, ans)

    m = C * 10 + B
    ans = verify(h, m, ans)
#####

##### 2
    h = B * 10 + A
    m = C * 10 + D
    ans = verify(h, m, ans)

    m = D * 10 + C
    ans = verify(h, m, ans)
    #
    h = B * 10 + C
    m = A * 10 + D
    ans = verify(h, m, ans)

    m = D * 10 + A
    ans = verify(h, m, ans)
    #
    h = B * 10 + D
    m = A * 10 + C
    ans = verify(h, m, ans)

    m = C * 10 + A
    ans = verify(h, m, ans)
#####

##### 3
    h = C * 10 + A
    m = B * 10 + D
    ans = verify(h, m, ans)

    m = D * 10 + B
    ans = verify(h, m, ans)
    #
    h = C * 10 + B
    m = A * 10 + D
    ans = verify(h, m, ans)

    m = D * 10 + A
    ans = verify(h, m, ans)
    #
    h = C * 10 + D
    m = A * 10 + B
    ans = verify(h, m, ans)

    m = B * 10 + A
    ans = verify(h, m, ans)
#####

##### 4
    h = D * 10 + A
    m = B * 10 + C
    ans = verify(h, m, ans)

    m = C * 10 + B
    ans = verify(h, m, ans)
    #
    h = D * 10 + B
    m = A * 10 + C
    ans = verify(h, m, ans)

    m = C * 10 + A
    ans = verify(h, m, ans)
    #
    h = D * 10 + C
    m = A * 10 + B
    ans = verify(h, m, ans)

    m = B * 10 + A
    ans = verify(h, m, ans)
#####

    return ans


#print(solution(1, 8, 3, 2))
print(solution(2, 3, 3, 2))