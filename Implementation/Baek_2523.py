"""
    @ Baek 2523 별 찍기 - 13
    @ Prob. https://www.acmicpc.net/problem/2523
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 23
    @ End day: 20. 01. 23
"""

N = int(input())
for i in range(1, N+1):
    print("*" * i)

for i in range(N-1, 0, -1):
    print("*" * i)



"""
3
>
*
**
***
**
*
"""