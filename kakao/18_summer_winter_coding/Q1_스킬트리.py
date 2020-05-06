"""
    @ 18 Summer winter coding: 스킬트린
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/49993
      Ref.
      Ref Prob.
    @ Algo: BFS
    @ Start day: 20. 05. 05.
    @ End day: 20. 05. 05.
"""

def solution(skill, skill_trees):
    ans = 0

    for skill_tree in skill_trees:
        tmp = []
        for ch in skill_tree:
            if ch in skill:
                tmp.append(ch)

        flag = True
        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                flag = False
                break
        if flag is True:
            ans += 1

    return ans


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2


