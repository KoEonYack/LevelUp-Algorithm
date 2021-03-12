'''



'''

arr = []
ans = None

def verify(H, M):
    if H <= 23 and H >= 0 and M>= 0 and M<=59 and [H, M] not in arr:
        arr.append([H, M])
        return ans+1
    else:
        return ans


def solution(A, B, C, D):
    global ans
    tmp = []
    A = "A" + str(A)
    B = "B" + str(B)
    C = "C" + str(C)
    D = "D" + str(D)

    for i in [A, B, C, D]:
        tmp.append(A)
        for j in [A, B, C, D]:
            if j in tmp:
                continue
            else:
                tmp.append(j)
            for k in [A, B, C, D]:
                if k in tmp:
                    continue
                else:
                    tmp.append(k)
                for l in [A, B, C, D]:
                    if l in tmp:
                        continue
                    else:
                        tmp.append(l)
                        print(tmp)
                        tmp.clear()

    return ans


print(solution(1, 8, 3, 2))
#print(solution(2, 3, 3, 2))