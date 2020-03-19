

digitKo = ["", "십", "백", "천", "만"]
numKo = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]

inputStr = input()
loc = len(inputStr) - 1
for i in inputStr:
    if i == "1":
        print(digitKo[loc], end="")
        if loc == 0:
            print("일", end="")
    elif i != "0":
        print(numKo[int(i)] + digitKo[loc], end="")
    loc -= 1


"""
input	answer
2001	"이천일"
98030	"구만팔천삼십"
11010	"만천십"
"""