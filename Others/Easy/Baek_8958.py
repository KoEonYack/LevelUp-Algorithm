"""
    @ Baek 8958 OX퀴즈
    @ Prob. https://www.acmicpc.net/problem/8958
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""


def check(inputStr):
    ans = 0
    flag = False
    wight = 1

    for char in inputStr:
        if char == 'O' and flag is True:    # 두번 이상 O 만난 경우
            ans += wight
            wight += 1
        elif char == 'O' and flag is False: # 처음 O 만난 경우
            flag = False
            ans += wight
            wight += 1
        else:                               # x의 경우
            flag = False
            wight = 1

    return ans

N = int(input())
for _ in range(N):
    inputStr = input()
    print(check(inputStr))


"""
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
>
10
9
7
55
30
"""