"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 : 호텔 방 배정
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64063
     Ref.   https://tech.kakao.com/2020/04/01/2019-internship-test/
    https://taxijjang.tistory.com/54

    @ Algo: 구현
    @ Start day: 20. 04. 28.
    @ End day: 20. 04. 28.
"""

from collections import deque

parent = dict()

def find(a):
    if parent[a] == 0:
        return a
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]

    return parent[a]


def solution(k, room_number):
    ans = deque()

    for room in room_number:
        next = find(room)
        ans.append(next)
        parent[next] = find(next+1)
        parent[room] = parent[next]

    return ans



k = 10
room_number = [1,3,4,1,3,1]
# k = 3
# room_number = [1, 3, 1, 1]

print(solution(k, room_number)) # [1,3,4,2,5,6]
