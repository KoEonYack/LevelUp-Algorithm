"""
    @ Baek 9085 더하기
    @ Prob. https://www.acmicpc.net/problem/9085
      Ref.
      Ref Prob.
    @ Algo:
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""

N = int(input())
for _ in range(N):
    M = int(input())
    print(sum(list(map(int, input().split()))))


"""
2
5
1 1 1 1 1
7
1 2 3 4 5 6 7
>
5
28
"""
