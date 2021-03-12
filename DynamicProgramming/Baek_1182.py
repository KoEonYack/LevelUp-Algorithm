"""
    @ 1182. 부분수열의 합
    @ Prob. https://www.acmicpc.net/problem/1182
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 31.
    @ End day: 20. 01. 31.
"""

def solution(idx, total_sum):
    global result

    if idx >= N:
        return
    total_sum += arr[idx]

    if total_sum == S:
        result += 1

    solution(idx+1, total_sum-arr[idx])
    solution(idx+1, total_sum)


result = 0
N, S = map(int, input().split())
arr = list(map(int, input().split()))

solution(0, 0)
print(result)

"""
5 0
-7 -3 -2 5 8
>
1
"""