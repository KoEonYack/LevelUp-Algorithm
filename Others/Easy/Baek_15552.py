"""
    백준 15552 알람 시계
    Prob https://www.acmicpc.net/problem/2884
    End Day : 2020. 1. 1
"""
import sys

N = int(input())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)


"""
5
1 1
12 34
5 500
40 60
1000 1000
>>
2
46
505
100
2000

"""