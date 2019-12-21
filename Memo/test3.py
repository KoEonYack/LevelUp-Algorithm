'''



'''


# Tree
def solution(S):
    dic = {}
    ans = 0
    partChar = 0
    flag = True
    dummyArr, tempArr = [], []

    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        dic[a] = False

    for i in range(0, len(S)-1): # Same char
        if S[i] == S[i+1] and flag == True:
            flag = True
        else:
            flag = False

    if flag == True:
        return len(S)

    i=0
    while True:
        partChar += 1
        print(tempArr)
        while True:
            if i+partChar < len(S):
                tempArr.append(S[i:i+partChar])
                i += 1
            else:
                i = 0
                break
        if partChar == len(S):
            break

    return ans


print(solution("dddd"))
print(solution("cycle"))
