"""
    @ 18 kako blind: 다트게임
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/17682
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 06.
    @ End day: 20. 05. 06.
"""

def solution(dartResult):
    total = 0
    i = 0
    tmp = 0
    prev = -1
    dartResult = dartResult.replace("10", "K")
    while i < len(dartResult):
        if dartResult[i].isdigit() or dartResult[i] == "K":
            prev = tmp
            total += tmp
            if dartResult[i] == "K":
                tmp = 10
            else:
                tmp = int(dartResult[i])
        elif dartResult[i] == "S":
            tmp *= 1
        elif dartResult[i] == "D":
            tmp = pow(tmp, 2)
        elif dartResult[i] == "T":
            tmp = pow(tmp, 3)
        elif dartResult[i] == "*":
            total = total + prev
            tmp *= 2
        elif dartResult[i] == "#":
            tmp *= -1
        i += 1

    return total + tmp


dartResult = "1D2S#10S"  # 9
dartResult = "1D2S0T"    # 3
dartResult = "1D2S3T*"   # 59
dartResult = "1S2D*3T"   # 37

# dartResult = "10S10S10S*"   # 59

print(solution(dartResult))

