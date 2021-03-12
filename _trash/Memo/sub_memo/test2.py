'''
    Prob 2.
'''

def solution(n):
    answer = 0
    kindOfNumArr = []

    nStr = str(n)
    for numStr in nStr:
        if int(numStr) not in kindOfNumArr and int(numStr) is not 0:
            kindOfNumArr.append(int(numStr))

    for num in kindOfNumArr:
        if int(nStr) % int(num) == 0:
            answer += 1

    return answer


print(solution(1234))
print(solution(2322))
