"""
    @ Baek 4101 크냐?
    @ Prob. https://www.acmicpc.net/problem/4101
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    elif A > B:
        print("Yes")
    else:
        print("No")


"""
1 19
4 4
23 14
0 0
>
No
No
Yes
"""

