"""
    백준 2884번 알람 시계
    Prob https://www.acmicpc.net/problem/2884
    End Day : 2020. 1. 1
"""

H, M = map(int, input().split())
nextM = M - 45
if nextM >= 0:
    print(H, nextM)
else:
    newH = H - 1
    if newH >= 0:
        print(newH, nextM+60)
    else:
        print(23, nextM+60)