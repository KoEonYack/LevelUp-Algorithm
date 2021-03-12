"""
    @ Baek 5576 콘테스트
    @ Prob. https://www.acmicpc.net/problem/5576
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 08
    @ End day: 20. 01. 08
"""

A = []
B = []
for _ in range(10):
    A.append(int(input()))
for _ in range(10):
    B.append(int(input()))

A.sort(reverse=True)
B.sort(reverse=True)
print(A[0]+A[1]+A[2], B[0]+B[1]+B[2])


"""
23
23
20
15
15
14
13
9
7
6
25
19
17
17
16
13
12
11
9
5
>
66 61
"""

