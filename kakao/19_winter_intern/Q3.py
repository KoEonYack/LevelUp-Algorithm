"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 : 불량사용자
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64064
     Ref. https://regularmember.tistory.com/192
    @ Algo: 구현
    @ Start day: 20. 04. 22.
    @ End day: 20. 04. 22.
"""

from itertools import permutations


def solution(user_ids, banned_ids):
    num_of_banned_user = len(banned_ids)
    ans = 0

    flag = False

    for candidate_users in permutations(user_ids, num_of_banned_user):

        for banned_id in banned_ids:
            if flag is True: break
            for candidate_user in candidate_users:
                if flag is True: break
                if len(banned_id) != len(candidate_user):
                    flag = True
                    continue

                for i in range(len(banned_id)):
                    if banned_id[i] == '*': continue
                    elif banned_id[i] != candidate_user[i]:
                        flag = True
                        break
                print(banned_id, candidate_user, flag)

        if flag is False:
            ans += 1
        else:
            flag = False

    return ans


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id)) # 2

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]
# print(solution(user_id, banned_id)) # 2

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"] # 2 2 2
# print(solution(user_id, banned_id))  # 3

