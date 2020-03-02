"""
    @ 프로그래머스 42588 탑
    @ Prob. https://www.acmicpc.net/problem/42588
     Ref.
    @ Algo: Deque
    @ Start day: 20. 03. 02.
    @ End day: 20. 03. 02.
"""

from collections import deque


def solution(heights):
    answer = deque([])
    flag = False
    
    for i in range(len(heights)-1, -1, -1):
        for j in range(i, -1, -1):
            if heights[j] > heights[i]:
                #print(heights[j])
                flag = True
                answer.appendleft(j+1)
                break

        if flag is False:
            answer.appendleft(0)
        flag = False

    return list(answer)



print(solution([6,9,5,7,4])) # [0,0,2,2,4]
print(solution([3,9,9,3,5,7,2])) # [0,0,0,3,3,3,6]
print(solution([1,5,3,6,7,6,5])) # [0,0,2,0,0,5,6]

