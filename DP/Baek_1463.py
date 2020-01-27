"""
    @ 1463. 1로 만들기
    @ Prob. https://www.acmicpc.net/problem/1463
     Ref.   https://chunghyup.tistory.com/49
    @ Algo: DP
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 27.
"""


N = int(input())
arr = [0] * (N+1)

arr[2] = 1
arr[3] = 1

for i in range(4, N+1):
    arr[i] += min(arr[i//2], arr[i//3], arr[i-1]) + 1

print(arr)
print(arr[N])

"""
2
>
1

"""