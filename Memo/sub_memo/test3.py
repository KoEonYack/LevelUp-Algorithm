

def checkParenthesis(smallStatus, middleStatus, largeStatus, flag):
    if (flag is 1 and smallStatus is not 0) or (flag is 2 and middleStatus is not 0 or smallStatus is not 0) or (largeStatus - 1 > 0) or (middleStatus - 1 > 0) or (smallStatus - 1 > 0):
        return False

def solution(inputStr):
    answer = False

    smallStatus, middleStatus, largeStatus = 0, 0, 0

    for char in inputStr:
        if char is "[":
            largeStatus += 1
            if checkParenthesis(smallStatus, middleStatus, largeStatus, flag=2) is False:
                break

        elif char is "{":
            middleStatus += 1
            if checkParenthesis(smallStatus, middleStatus, largeStatus, flag=1) is False:
                break

        elif char is "(":
            smallStatus += 1
        elif char is ")":
            smallStatus -= 1
            if checkParenthesis(smallStatus, middleStatus, largeStatus, flag=3) is False:
                break

        elif char is "}":
            middleStatus -= 1
        elif char is "]":
            largeStatus -= 1

    if largeStatus is 0 and middleStatus is 0 and smallStatus is 0:
        answer = True

    return answer

#print(solution("3+[(5+1)-1]"))
#print(solution("3+([5+1])"))
#print(solution("3+{(5+1}"))
#print(solution("3+([5+1])"))
#print(solution("3+[{(5+1)-1}+3]"))
print(solution(" { { } } "))
print(solution("3+[(5+1)-1]"))
print(solution("3+[{( )}{}]"))
print(solution("[[]]"))
print(solution("(())"))
