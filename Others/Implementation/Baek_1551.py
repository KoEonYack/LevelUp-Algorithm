"""
    @ Baek 1551 수열의 변화
    @ Prob. https://www.acmicpc.net/problem/1551
      Ref.
      Ref Prob.
    @ Algo: 시뮬레이션
    @ Start day: 20. 03. 31.
    @ End day: 20. 03. 31.
"""

N, K = map(int, input().split())
arr = list(map(int, input().split(",")))

for i in range(K):
    for j in range(N-(i+1)):
        arr[j] = arr[j+1] - arr[j]

print(arr[0], end="")
for i in range(1, N-K):
    print(","+ str(arr[i]), end="")


"""
5 1
5,6,3,9,-1
>
1,-3,6,-10
"""