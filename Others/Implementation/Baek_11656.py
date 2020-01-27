"""
    @ Baek 11656 접미사 배열
    @ Prob. https://www.acmicpc.net/problem/11656
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 27
    @ End day: 20. 01. 27
"""

inputStr = input()
ansArr = []
for i in range(len(inputStr)):
    ansArr.append(inputStr[i:])

ansArr.sort()
print("\n".join(ansArr))

"""
baekjoon
>
aekjoon
baekjoon
ekjoon
joon
kjoon
n
on
oon
"""