"""
    @ Baek 11721
    @ Prob. https://www.acmicpc.net/problem/11721
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

inputStr = input()
cnt = 0
for ch in inputStr:
    cnt += 1
    print(ch, end="")
    if cnt % 10 == 0:
        print()



"""
OneTwoThreeFourFiveSixSevenEightNineTen
>
OneTwoThre
eFourFiveS
ixSevenEig
htNineTen

BaekjoonOnlineJudge
>
BaekjoonOn
lineJudge
"""