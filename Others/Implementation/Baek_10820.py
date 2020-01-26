"""
    @ Baek 10820 문자열 분석
    @ Prob. https://www.acmicpc.net/problem/10820
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""


while True:
    try:
        inputStr = input()
        digit = 0
        low = 0
        cap = 0
        white = 0
    except:
        break
    for ch in inputStr:
        if '0' <= ch <= '9':
            digit += 1
        elif 'a' <= ch <= 'z':
            low += 1
        elif 'A' <= ch <= "Z":
            cap += 1
        elif ch == " ":
            white += 1

    print(low, cap, digit, white)


"""
This is String
SPACE    1    SPACE
 S a M p L e I n P u T     
0L1A2S3T4L5I6N7E8
>
10 2 0 2
0 10 1 8
5 6 0 16
0 8 9 0
"""
