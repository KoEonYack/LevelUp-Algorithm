"""
    @ Baek 17087 숨바꼭질 6
    @ Prob. https://www.acmicpc.net/problem/17087
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""

from math import gcd

# 입력 갯수, 동생 위치
N, S = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(N):
    arr[i] = abs(arr[i] - S)

if N > 2:
    num = gcd(arr[0], arr[1])
    for i in range(2, N):
        num = gcd(num, arr[i])
elif N > 1:
    num = gcd(arr[0], arr[1])
else:
    num = arr[0]
print(num)


"""
3 3
1 7 11
>
2
-------------
3 81
33 105 57
>
24
"""