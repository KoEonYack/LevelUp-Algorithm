"""
    @ Baek 10093 숫자
    @ Prob. https://www.acmicpc.net/problem/10093
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""


A, B = map(int, input().split())
if A == B:
    print(0)
else:
    if A > B:
        A, B = B, A
    print(B-A-1)
    for num in range(A, B-1):
        print(num+1, end=" ")


"""
8 14
>
5
9 10 11 12 13
"""