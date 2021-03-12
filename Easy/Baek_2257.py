"""
    @ Baek 2577 숫자의 개수
    @ Prob. https://www.acmicpc.net/problem/2577
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 05
    @ End day: 20. 01. 05
"""

from collections import Counter

A = int(input())
B = int(input())
C = int(input())

mul_num = list(str(A * B * C))
for i in range(10):
    num_count = mul_num.count(str(i))
    print(num_count)

"""
150
266
427
>
3
1
0
2
0
0
0
2
0
0
"""
