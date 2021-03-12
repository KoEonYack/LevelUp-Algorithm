'''



'''

def solution(S):
    ans = ""
    count = 1
    flag2, flag1 = False, False
    S = S.replace("-", "").replace(" ", "")
    twoFlag = False

    if len(S) >= 2 and len(S) <= 3 : # Min case
        return S

    if len(S) % 3 == 2:
        flag1 = True
    elif len(S) % 3 == 1:
        flag2 = True

    if (flag1 == True) or (flag1 == False and flag2 == False):
        for i in range(len(S)):
            ans += str(S[i])
            if (i+1) % 3 == 0 and i != (len(S) - 1):
                ans += "-"
    if flag2 == 1:
        for i in range(len(S)):
            ans += str(S[i])

            if len(S) == ((count) * 3 + 1):
                twoFlag = True
            elif (i+1) % 3 == 0:
                ans += "-"
                count += 1

            if twoFlag == True:
                if (i + 1) % 2 == 0 and i != (len(S) - 1) :
                    ans += "-"

    return ans

#print(solution("00-44  48 5555 8361"))
#print(solution("0 - 22 1985--324")) # 1
#print(solution("555372654"))
print(solution("023"))