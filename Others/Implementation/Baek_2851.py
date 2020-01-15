"""
    @ Baek 2851 슈퍼 마리오
    @ Prob. https://www.acmicpc.net/problem/2851
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 14
    @ End day: 20. 01. 14
"""

arr = [int(input()) for _ in range(10)]

Sum = 0
for i in range(10):
    afterSum = Sum + arr[i]
    if afterSum >= 100:
        if afterSum - 100 <= 100 - Sum:
            print(afterSum)
        else:
            print(Sum)
        exit(0)
    Sum = afterSum

print(Sum)


"""
10
20
30
40
50
60
70
80
90
100
>
100
"""