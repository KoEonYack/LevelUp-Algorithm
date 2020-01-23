"""
    @ Baek 10174 팰린드롬
    @ Prob. https://www.acmicpc.net/problem/10174
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 24
    @ End day: 20. 01. 24
"""


for i in range(int(input())):
    inputStr = str(input()).upper()
    if inputStr == inputStr[::-1]:
        print("Yes")
    else:
        print("No")

"""
6
Nat tan
Palindrome 
123454321
Dogs and Cats
**()()**
1 221
>
Yes
No
Yes
No
No
No
"""