"""
    @ Baek 2251 물통 ?
    @ Prob. https://www.acmicpc.net/problem/2251
      Ref.
      Ref Prob.
    @ Algo: Brute-force
    @ Start day: 20. 01. 29
    @ End day: 20. 01. 29
"""

# 8 9 10
A, B, C = map(int, input().split())
arr = []

if C-B > 0:
    arr.append(C-B)
if C-A > 0:
    arr.append(C-A)
arr.append(A)
arr.append(B)
arr.append(C)

res = list(set(arr))
res.sort()
print(*res)

"""
8 9 10
>
1 2 8 9 10
"""