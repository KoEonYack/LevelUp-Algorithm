'''
    Part3 - Prob1. : String
'''


def solution(s):
    ans = 0
    score = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j] == "L":
                score += 1
            elif s[j] == "R":
                score -= 1
            elif s[j] == "U":
                score += 100
            elif s[j] == "D":
                score -= 100
            else:
                print("Error")

            if score == 0:
                ans += 1
                score = 0
        score = 0

    return ans


print(solution("URLLDRLR"))
