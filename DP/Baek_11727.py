"""
    @ 11727. 2×n 타일링 2
    @ Prob. https://www.acmicpc.net/problem/11727
     Ref.   https://ecycle.tistory.com/1
    @ Algo: DP
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 27.
"""

arr = [0, 1, 3]
for i in range(3, 1001):
    arr.append(arr[i - 2] * 2 + arr[i - 1])
N = int(input())
print(arr[N] % 10007)

"""
12
>
2731
"""