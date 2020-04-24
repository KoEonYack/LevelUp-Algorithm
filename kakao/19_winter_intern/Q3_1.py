"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 : 불량사용자
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64064
     Ref. https://regularmember.tistory.com/192
    @ Algo: 구현
    @ Start day: 20. 04. 22.
    @ End day: 20. 04. 22.
"""

from itertools import permutations


def isMatchId(ban_id, user_id):
    for i in range(len(ban_id)):
        if ban_id[i] == '*': continue
        elif ban_id[i] != user_id[i]:
            return False
    return True

# ['fr*d*', 'abc1**'] ('frodo', 'fradi')
def check(banned_ids, candidate_users):
    for i in range(len(banned_ids)):
        if len(banned_ids[i]) != len(candidate_users[i]):
            return False
        if isMatchId(banned_ids[i], candidate_users[i]) is False:
            return False
    return True


def solution(user_ids, banned_ids):
    ans = list()

    for candidate_users in permutations(user_ids, len(banned_ids)):
        if check(banned_ids, candidate_users) is True:
            candidate_users = set(candidate_users)
            if candidate_users not in ans:
                ans.append(candidate_users)

    return len(ans)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id)) # 2

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]
# print(solution(user_id, banned_id)) # 2
#
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"] # 2 2 2
# print(solution(user_id, banned_id))  # 3

