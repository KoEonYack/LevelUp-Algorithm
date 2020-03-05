"""
    @ Baek 2921 도미노
    @ Prob. https://www.acmicpc.net/problem/2953
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""

N = int(input())
ans = 0
for i in range(0, N+1):
    for j in range(i, N+1):
        ans += (i + j)
print(ans)

"""
2
>
12
"""