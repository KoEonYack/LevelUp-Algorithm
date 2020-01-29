"""
    @ 백준 1977 완전제곱수
    @ https://www.acmicpc.net/problem/1977
    @ End Day : 2020. 01. 29.
"""

N = int(input())
M = int(input())

i = 1
arr = []
while i * i <= M:
    if N <= i * i <= M:
        arr.append(i*i)
    i += 1

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])

"""
60
100
>
245
64
"""