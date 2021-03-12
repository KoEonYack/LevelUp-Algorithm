"""
    @ Baek 5598 카이사르 암호
    @ Prob. https://www.acmicpc.net/problem/5598
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""

inputStr = input()
startChar = ord('A')
endCharAscii = ord('Z')
for char in inputStr:
    if ord(char) - 3 < startChar:
        print(startChar - (ord(char) - 3))
        print(chr(endCharAscii - (startChar - (ord(char) - 3))), end="")
    else:
        print(chr(ord(char) - 3), end="")

"""
ABC
>
1 2 3 4 5
W X Y Z A
HIJKLMNOPQRSTU

MRL
>
JOI
"""