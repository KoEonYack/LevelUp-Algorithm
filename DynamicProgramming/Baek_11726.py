"""
    @ 11726. 2×n 타일링
    @ Prob. https://www.acmicpc.net/problem/11726
     Ref.   https://hongku.tistory.com/277
    @ Algo: DP
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 27.
"""

arr = [0, 1, 2]
for i in range(3, 1001):
    arr.append(arr[i - 2] + arr[i - 1])
N = int(input())
print(arr[N] % 10007)

"""
2
>
2

9
>
55
"""