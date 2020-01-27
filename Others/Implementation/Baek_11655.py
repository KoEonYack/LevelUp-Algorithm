"""
    @ Baek 11655 ROT13
    @ Prob. https://www.acmicpc.net/problem/11655
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 26
    @ End day: 20. 01. 26
"""

cap_arr = [chr(ord('A') + i) for i in range(26)]
small_arr = [chr(ord('a') + i) for i in range(26)]
inputStr = input()

for ch in inputStr:
    if ch.isalpha() is True:
        if ch.isupper():
            print(cap_arr[(cap_arr.index(ch) + 13)%26], end="")
        else:
            print(small_arr[(small_arr.index(ch) + 13)%26], end="")
    else:
        print(ch, end="")


"""
Baekjoon Online Judge
>
Onrxwbba Bayvar Whqtr
----------------------------------
One is 1
>
Bar vf 1
"""