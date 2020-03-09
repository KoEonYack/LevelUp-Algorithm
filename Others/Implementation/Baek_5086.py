"""
    @ Baek 5086 배수와 약수
    @ Prob. https://www.acmicpc.net/problem/5086
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")


"""
8 16
32 4
17 5
0 0 
>   
factor
multiple
neither
"""