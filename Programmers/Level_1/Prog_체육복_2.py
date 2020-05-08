"""
    @ 프로그래머스 : 체육복
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42862
      Ref. https://chibychi.blogspot.com/2019/04/24-python.html
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(n, lost, reserve):
    reserve = [r for r in reserve if r not in lost]
    lost = [l for l in lost if l not in reserve]

    for num in lost:
        if num in reserve:
            reserve.remove(num)
        elif num-1 in reserve:
            reserve.remove(num-1)
        elif num+1 in reserve:
            reserve.remove(num+1)
        else:
            n -= 1

    return n


n = 5
lost = [2, 4]
revserve = [1, 3, 5]
revserve = [3]
print(solution(n, lost, revserve))
