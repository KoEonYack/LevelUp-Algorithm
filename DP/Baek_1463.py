"""
    @ 1463. 1로 만들기
    @ Prob. https://www.acmicpc.net/problem/1463
     Ref.   https://chunghyup.tistory.com/49
    @ Algo: DP
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 30.
"""


N = int(input())
arr = [0] * (N+1)

arr[0] = 0
arr[1] = 0

for i in range(2, N+1):
    tmp_min = N + 1
    if i % 3 == 0:
        tmp_min = min(tmp_min, arr[i // 3])

    if i % 2 == 0:
        tmp_min = min(tmp_min, arr[i // 2])
        arr[i] += arr[i//2]

    tmp_min = min(tmp_min, arr[i-1])
    arr[i] = tmp_min + 1

print(arr[-1])

"""
2
>
1
"""