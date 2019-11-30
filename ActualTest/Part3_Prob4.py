'''
    Part3 - Prob4. : DP
    print(solution(6, [[1,2],[2,3],[4,5]]))
'''

def solution(numberArr, startArr, endArr):
    ansArr = []
    sumDP = []
    sumDP.append(numberArr[0])

    for i in range(1, len(numberArr)):
        sumDP.append(sumDP[i-1] + numberArr[i])

    print(sumDP)

    for i in range(len(startArr)):
        ansArr.append(sumDP[endArr[i]] - sumDP[startArr[i]-1])

    return ansArr


print(solution([100, 101, 102, 103, 104], [1, 2], [2, 4]))