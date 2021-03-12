"""
    @ Baek 10474 분수좋아해?
    @ Prob. https://www.acmicpc.net/problem/10474
      Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A//B, end=" ")
    print(A%B, end=" ")
    print("/", end=" ")
    print(B, end=" ")
    print()



"""
27 12
2460000 98400
3 4000
0 0
>
2 3 / 12
25 0 / 98400
0 3 / 4000

"""