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


def solution(str1, str2):
    s1_l = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
    s2_l = [str2[i:i + 2].lower() for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    if len(s1_l) == 0 and len(s2_l) == 0:
        return 65536

    mset_s1 = mset(s1_l)
    mset_s2 = mset(s2_l)

    interSetLen = len(list((mset_s1 & mset_s2).elements()))
    unionSetLen = len(list((mset_s1 | mset_s2).elements()))


    return int(interSetLen / unionSetLen *65536)


str1 = "FRANCE"
str2 = "french"

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2)) # 16384
