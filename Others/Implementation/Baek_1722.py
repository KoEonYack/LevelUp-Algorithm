"""
    @ Baek 1722 순열의 순서
    @ Prob. https://www.acmicpc.net/problem/1722
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 01. 13
    @ End day: 20. 01. 13
"""


N = int(input())
arr = list(map(int, input().split()))
f = [0] * 21
check = [False] * 21
numArr = []

for i in range(1, 21):
    f[i] = f[i-1] * i

if arr[0] == 1:    # arr[1] 번째 수열 값을 찾는 과정
    pass

elif arr[1] == 2:  # K번째 수열을 찾는 과정
    for i in range(N):
        for j in range(1, N+1):
            if check[j] is True:
                continue
            if f[N-i-1] < arr[1]:
                arr[1] -= f[N-i-1]
            else:
                numArr[i] = j
                check[j] = True
                break

    for val in arr:
        print(val, end=" ")

"""
4
2 1 3 2 4
>
3
"""
