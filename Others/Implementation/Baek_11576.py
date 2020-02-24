"""
    @ Baek 11576 Base Conversion
    @ Prob. https://www.acmicpc.net/problem/11576
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 24.
    @ End day: 20. 02. 24.
"""

A, B = map(int, input().split())
M = int(input())
arr = list(map(int, input().split()))
result = []
base_10 = 0

i = 0
arr.reverse()
for num in arr:
    base_10 += (num*pow(A, i))
    i += 1

while base_10:
    result.append(base_10 % B)
    base_10 //= B

result.reverse()
print(*result)

"""
17 8
2
2 16
>
6 2
"""