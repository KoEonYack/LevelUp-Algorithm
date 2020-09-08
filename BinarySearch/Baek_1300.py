"""
    @ Baek 1300. K번째 수
    @ Prob. https://www.acmicpc.net/problem/1300
     Ref.   https://claude-u.tistory.com/449
    @ Algo: Binary Search
    @ Start day: 20. 08. 29.
    @ End day: 20. 08. 29.
"""

N, K = int(input()), int(input())
start, end = 1, K
ans = 0

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for i in range(1, N+1):
        tmp += min(mid//i, N)
        # mid 이하 i 배수 or N

    if tmp >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)




"""
3
7
>
6
"""
