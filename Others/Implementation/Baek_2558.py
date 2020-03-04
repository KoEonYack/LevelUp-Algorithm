"""
    @ Baek 2558 곱셈
    @ Prob. https://www.acmicpc.net/problem/2558
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

A = int(input())
B = input()

for num in B[::-1]:
    print(A * int(num))
print(A*int(B))

"""
472
385
>
2360
3776
1416
181720
"""