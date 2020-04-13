"""
    @ Baek 9243 파일 완전 삭제
    @ Prob. https://www.acmicpc.net/problem/9243
      Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 13.
    @ End day: 20. 04. 13.
"""

N = int(input())
S = input()
K = input()
res = ""
if N % 2 != 0:
    for ch in S:
        if ch == "0":
            res += "1"
        else:
            res += "0"
else:
    res = S

if res == K:
    print("Deletion succeeded")
else:
    print("Deletion failed")


"""
1
10001110101000001111010100001110
01110001010111110000101011110001
>
Deletion succeeded
--------------------------------
20
0001100011001010
0001000011000100
>
Deletion failed    

"""