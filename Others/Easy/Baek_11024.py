"""
    백준 11024 더하기 4
    End Day : 2020. 01. 28.
"""

N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    print(sum(arr))

"""
2
1 2 3 4 5
5 4 5 4 2 3 1 2
>
15
26
"""