"""
    @ Baek 11068 회문인 수
    @ Prob. https://www.acmicpc.net/problem/11068
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 04. 09.
    @ End day: 20. 04. 09.
"""

def pali(s):
    s = [str(i) for i in s]
    if s == s[::-1]:
        return True
    return False

def N_Digit_arr(b, x):
    arr = []
    while x > 0:
        arr.append(x % b)
        x = x // b
    return arr

def makeDigit(num):
    arr = []
    for i in range(2, 65): # 65
        if pali(N_Digit_arr(i, num)):
            return True
    return False

for _ in range(int(input())):
    N = int(input())
    if makeDigit(N):
        print(1)
    else:
        print(0)



"""
3
747
255
946734
>
1
1
0
"""
