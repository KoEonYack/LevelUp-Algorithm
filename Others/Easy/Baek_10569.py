"""
    백준 10569번 다면체
    Prob https://www.acmicpc.net/problem/10569
    End Day : 2020. 01. 28.
"""

N = int(input())
for _ in range(N):
    V, E = map(int, input().split())
    print(E-V+2)


"""
2
8 12
4 6
>
6
4
"""
