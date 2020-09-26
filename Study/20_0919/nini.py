import copy

INF = 200000000

import sys

def solution(stones, k):
    left = 1;
    right = INF

    while left <= right:
        mid = (left + right) // 2
        tmp = copy.deepcopy(stones)
        for i in range(len(tmp)):
            tmp[i] -= mid


        cnt = 0
        check = False
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                check = True
                break

        if check is True:
            right = mid - 1
        else:
            left = mid + 1

    return left