"""
    @ Baek 3062 수 뒤집기
    @ Prob. https://www.acmicpc.net/problem/3062
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

for _ in range(int(input())):
    A = input()
    revA = A[::-1]
    res = int(A) + int(revA)

    if str(res) == str(res)[::-1]:
        print("YES")
    else:
        print("NO")


"""
4
13
58
120
5056
>
YES
NO
YES
NO
"""