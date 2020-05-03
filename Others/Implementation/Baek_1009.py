"""
    @ Baek 1009 분산처리
    @ Prob. https://www.acmicpc.net/problem/1009
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 02.
    @ End day: 20. 05. 02.
"""

for i in range(int(input())):
    A, B = map(int, input().split())
    print(pow(A, B) % 10)

"""
5
1 6
3 7
6 2
7 100
9 635
>
1
7
6
1
9

"""