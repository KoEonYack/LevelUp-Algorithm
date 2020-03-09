"""
    @ Baek 1026 보물
    @ Prob. https://www.acmicpc.net/problem/1026
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 03. 09.
    @ End day:  20. 03. 09.
"""


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
total = 0
for i in range(N):
    total += A[i] * B[i]
print(total)

"""
5
1 1 1 6 0
2 7 8 3 1
>
18
"""