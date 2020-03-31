"""
    @ Baek 1333 부재중 전화
    @ Prob. https://www.acmicpc.net/problem/1333
      Ref.
      Ref Prob.
    @ Algo: 시뮬레이션
    @ Start day: 20. 03. 31.
    @ End day: 20. 03. 31.
"""

N, L, D = map(int, input().split())
arr = []
for i in range(N):
    for j in range(L):
        arr.append(1)
    for j in range(5):
        arr.append(0)

bell = 0
while True:
    if bell >= len(arr):
        break
    if arr[bell] == 0:
        break
    else:
        bell += D

print(bell)

"""
2 5 7
>
7
"""