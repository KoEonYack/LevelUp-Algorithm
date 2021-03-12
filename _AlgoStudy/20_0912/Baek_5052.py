"""
    @ Baek 5052 전화번호 목록
    @ Prob. https://www.acmicpc.net/problem/5052
      Ref.
    @ Algo:
    @ Start day: 20. 09. 12.
    @ End day: 20. 09. 12.
"""

from sys import stdin
input = stdin.readline

def solution():
    data.sort()
    for i in range(N-1):
        if data[i] == data[i+1][:len(data[i])]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    data = list()
    N = int(input())
    for _ in range(N):
        data.append(input().rstrip())

    print(solution())

"""
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
>
NO
YES

"""