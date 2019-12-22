'''
    @ Baek 11047
    @ Prob. https://www.acmicpc.net/problem/11047
      Ref.
            https://kswims.tistory.com/173
            https://www.crocus.co.kr/678
      Ref Prob.
    @ Algo: Greedy
    @ Start day: 19. 12. 21
    @ End day: 19. 12.
'''


def solution(inputPriceArr):
    global Price
    answer = 0
    for i in range(InputLen):
        if Price // inputPriceArr[i] > 0:
            answer += (Price // inputPriceArr[i])
            Price -= inputPriceArr[i] * (Price // inputPriceArr[i])

    return answer


InputLen, Price= map(int, input().split())
inputPriceArr = []
for i in range(InputLen):
    inputPriceArr.append(int(input()))

inputPriceArr.sort(reverse=True)
print(solution(inputPriceArr))

'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''