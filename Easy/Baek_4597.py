"""
    @ Baek 4597. 패리티
    @ Prob. https://www.acmicpc.net/problem/4597
      Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 13.
    @ End day: 20. 04. 13.
"""

while True:
    S = input()
    if S == '#': break
    if S[-1] == 'e':             # 짝수 패라티
        if S.count("1") % 2 != 0:
            S = S.replace("e", "1")
            print(S)
        else:
            S = S.replace("e", "0")
            print(S)
    elif S[-1] == 'o':           # 홀수 패라티
        if S.count("1") % 2 != 0:
            S = S.replace("o", "0")
            print(S)
        else:
            S = S.replace("o", "1")
            print(S)



"""
101e
010010o
1e
000e
110100101o
#
>
1010
0100101
11
0000
1101001010

"""