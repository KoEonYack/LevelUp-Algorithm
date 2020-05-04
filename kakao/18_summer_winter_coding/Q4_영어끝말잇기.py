"""
    @ 18 Summer winter coding: 영어 끝말잇기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12981
      Ref.
      Ref Prob.
    @ Algo:
    @ Start day: 20. 05. 04.
    @ End day: 20. 05. 04.
"""


def solution(n, words):
    part = 1
    human = -1
    prev_word = words[0][-1]
    flag = False
    for i in range(1, len(words)):
        if i % n == 0:
            part += 1
        if prev_word != words[i][0] or words[i] in words[:i]:
            human = i
            flag = True
            break
        prev_word = words[i][-1]

    if flag is False:
        return [0, 0]
    return [human % n + 1, part]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# [3, 3]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
# [1, 3]
