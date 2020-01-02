"""
    @ Baek 1654
    @ Prob. https://www.acmicpc.net/problem/1654
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 19. 12. 31
    @ End day: 19. 12. 31
"""

import sys

def solution():
    answer = 0
    start = 0
    end = sys.maxsize

    while start <= end:
        mid = (start + end) // 2
        result = 0

        for i in range(0, N):
            result += arr[i] // mid

        if result >= M:
            start = mid + 1
            print(start, end)
            if mid > answer:
                answer = mid
        else:
            end = mid - 1

    return answer


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
print(solution())



"""
4 11
802
743
457
539

> 200
"""