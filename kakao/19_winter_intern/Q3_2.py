"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 : 불량사용자
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64064
     Ref. https://regularmember.tistory.com/192
    @ Algo: 구현
    @ Start day: 20. 04. 22.
    @ End day: 20. 04. 22.
"""

from itertools import permutations, combinations


def isMatch(bann, users):
    for i in range(len(bann)):
        if bann[i] == '*': continue
        elif bann[i] != users[i]:
            return False
    return True

# ['fr*d*', 'abc1**'] ('frodo', 'fradi')
def check(banned_ids, candidate_users):
    len_ids = len(banned_ids)
    # print("------------------------------------")
    for i in range(len_ids):
        if len(banned_ids[i]) != len(candidate_users[i]):
            return False
        # print(banned_ids[i], candidate_users[i], i)
        if isMatch(banned_ids[i], candidate_users[i]) is False:
            return False

    return True

ans_set = list()

def solution(user_ids, banned_ids):
    num_of_banned_user = len(banned_ids)
    ans = 0

    for a in permutations(user_ids, num_of_banned_user):
        print(a)

    for candidate_users in permutations(user_ids, num_of_banned_user):
        if check(banned_ids, candidate_users) is True:
            # candidate_users = set(candidate_users)
            # print("D", candidate_users)
            ans_set.append(candidate_users)
            ans += 1
            print("Ans", banned_ids, candidate_users)

    test = ans_set
    # print(ans_set)
    return ans


# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]
# print(solution(user_id, banned_id)) # 2

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id)) # 2
#
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"] # 2 2 2
# print(solution(user_id, banned_id))  # 3

