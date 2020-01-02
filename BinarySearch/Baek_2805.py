"""
    @ Baek 2805
    @ Prob. https://www.acmicpc.net/problem/2805
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 19. 12. 31
    @ End day: 20. 1. 1
"""

import sys


def solution():
    answer = 0
    start = 0
    end = sys.maxsize # max(arr)

    while start <= end:
        mid = (start + end) // 2
        remain_sum = 0

        for i in range(0, N):
            remain_ele = arr[i] - mid
            if remain_ele > 0:
                remain_sum += remain_ele

        if remain_sum >= M:
            start = mid + 1
            if mid > answer:
                answer = mid
        else:
            end = mid - 1

    return answer


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(solution())

"""
4 7
20 15 10 17

>> 15
"""

