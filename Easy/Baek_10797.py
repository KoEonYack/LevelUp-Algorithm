"""
    @ Baek 10797 10부제
    @ Prob. https://www.acmicpc.net/problem/10797
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""

Day = int(input())
arr = list(map(int, input().split()))
print(arr.count(Day))

"""
1
1 2 3 4 5
>
5


1 3 0 7 4
>
0
"""