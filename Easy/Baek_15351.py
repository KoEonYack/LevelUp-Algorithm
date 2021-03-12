"""
    백준 15351 인생 점수
    Prob https://www.acmicpc.net/problem/15351
    End Day : 2020. 4. 14.
"""

for _ in range(int(input())):
    S = input().replace(" ", "")
    res = 0
    for ch in S:
        res += (ord(ch) - ord('A') + 1)
    if res == 100:
        print("PERFECT LIFE")
    else:
        print(res)


"""
4
OTAKU LIFE
PRODUCER
GAMING LIFE
PROGRAMMING
>
PERFECT LIFE
PERFECT LIFE
83
131
"""