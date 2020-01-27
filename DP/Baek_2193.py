"""
    @ 2193. 이친수
    @ Prob. https://www.acmicpc.net/problem/2193
     Ref.   https://hongku.tistory.com/277
    @ Algo: DP
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 27.
"""

N = int(input())
arr = [0, 1, 1]

for i in range(3, N+1):
    arr.append(arr[i-1] + arr[i-2])
print(arr[-1])


"""
3
>
2
"""