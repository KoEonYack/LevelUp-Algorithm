"""
    @ 18 kako blind: 뉴스 클러스터링
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/17677
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 06.
    @ End day: 20. 05. 06.
"""

import re
from collections import Counter as mset

p = re.compile("[A-Z]{2}")

def setCollector(s):
    s_l = []
    for i in range(len(s)-1):
        if p.match(s[i:i+2]):
            s_l.append(s[i:i+2])
    return s_l


def solution(str1, str2):
    s1_l = setCollector(str1.upper())
    s2_l = setCollector(str2.upper())

    if len(s1_l) == 0 and len(s2_l) == 0:
        return 65536

    mset_s1 = mset(s1_l)
    mset_s2 = mset(s2_l)
    # print(mset_s1)
    # print(mset_s2)
    # print("----------------")
    # print(mset_s1 & mset_s2)

    interSetLen = len(list((mset_s1 & mset_s2).elements()))
    unionSetLen = len(list((mset_s1 | mset_s2).elements()))
    # print(list((mset_s1 & mset_s2).elements()))
    # print(list(mset_s1 | mset_s2).elements()))
    #
    # interSet = mset_s1 & mset_s2
    # unionSet = mset_s1 | mset_s2

    return int(interSetLen / unionSetLen *65536)

str1 = "FRANCE"
str2 = "french"

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2)) # 16384
