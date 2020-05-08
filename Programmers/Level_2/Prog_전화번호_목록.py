"""
    @ 프로그래머스 : 전화번호 목록
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42577
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""


def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                print(phone_book[i], phone_book[j])
                return False
            elif phone_book[j].startswith(phone_book[i]):
                return False
    return True



# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123","456","789"]
print(solution(phone_book))