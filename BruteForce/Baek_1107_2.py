"""
    @ Baek 1107. 크게 만들기
    @ Prob. https://www.acmicpc.net/problem/1107
     Ref.
    @ Algo: Brute force
    @ Start day: 20. 08. 25.
    @ End day: 20. 08. 25.
"""

N = int(input())
M = int(input())
enable = set(str(i) for i in range(10))

banned = set()
if M != 0:
    banned = set(map(str, input().split()))
    enable -= banned

min_count = abs(100 - N)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if num[j] in banned:
            break
        elif j == len(num) - 1:
            min_count = min(min_count, abs(N - int(num)) + len(str(num)))

print(min_count)

"""
5457
3
6 7 8
>
6
-------------------
500000
8
0 2 3 4 6 7 8 9
>
11117
"""