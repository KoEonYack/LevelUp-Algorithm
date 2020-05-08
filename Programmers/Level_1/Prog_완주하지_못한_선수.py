"""
    @ 프로그래머스 : 완주하지 못한 선수
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42576
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

from collections import Counter as mset

def solution(participant, completion):
    return list(mset(participant) - mset(completion))[0]

participant = ["leo", "kiki", "eden"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["eden", "kiki"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))