"""
    @ Baek 2752 세수정렬
    @ Prob. https://www.acmicpc.net/problem/2752
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

a, b, c = map(int, input().split())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("{} {} {}".format(a, b, c))

"""
3 1 2
>
1 2 3
"""
