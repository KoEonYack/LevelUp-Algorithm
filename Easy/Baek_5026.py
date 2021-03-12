"""
    @ Baek 5026. 박사 과정
    @ Prob. https://www.acmicpc.net/problem/5026
      Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""

for _ in range(int(input())):
    inputStr = input()
    if inputStr == "P=NP":
        print("skipped")
    else:
        A, B = map(int, inputStr.split("+"))
        print(A+B)

"""
4
2+2
1+2
P=NP
0+0
>
4
3
skipped
0
"""