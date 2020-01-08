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
arr = [chr(i) for i in range(ord('A'), ord('Z')+1)]
for char in inputStr:
    idx = ord(char) - ord('A')
    if idx - 3 < 0:
        print(arr[len(arr) - abs(idx - 3)], end="")
    else:
        print(arr[idx-3], end="")

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