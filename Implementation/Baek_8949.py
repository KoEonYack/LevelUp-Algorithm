"""
    @ Baek 8949 대충 더해
    @ Prob. https://www.acmicpc.net/problem/8949
      Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""


A, B = map(str, input().split())
buff = abs(len(A) - len(B))
if len(A) > len(B):
    B = "0" * buff + B
else:
    A = "0" * buff + A

for i in range(len(A)):
    print(str(int(A[i])+int(B[i])), end="")

"""
512 444
>
956
-----------
123 2495
"""


