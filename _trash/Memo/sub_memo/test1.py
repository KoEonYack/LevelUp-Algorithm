'''
    Prob 1.
'''

def solution(minPrice, maxPrice, budget):
    answer = 0
    currentBudget = budget

    if minPrice > maxPrice:
        minPrice, maxPrice = maxPrice, minPrice

    i = 0
    while True:
        maxPriceCost = maxPrice * i
        currentBudget = budget - maxPriceCost
        if currentBudget < 0 :
            break
        if currentBudget % minPrice is 0:
            answer += 1
        i += 1

    return answer

print(solution(3000, 5000, 23000))