"""
    백준 2495 연속구간
    Prob https://www.acmicpc.net/problem/2495
    End Day : 2020. 4. 14.
"""

for _ in range(3):
    S = input()
    res = 1
    maxV = -1
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            res += 1
        else:
            if maxV < res:
                maxV = res
            res = 1
    if maxV < res:
        maxV = res
    print(maxV)


"""
12345123
17772345
88888888
22233331
"""