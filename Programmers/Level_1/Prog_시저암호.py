"""
    @ 프로그래머스 : 시저암호
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12926
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(s, n):
    cap = [chr(i) for i in range(ord("A"), ord("Z")+1)]
    low = [chr(i) for i in range(ord("a"), ord("z")+1)]
    ans = ""
    for ch in s:
        if ch in cap:
            ans += cap[(cap.index(ch) + n) % 26]
        elif ch in low:
            ans += low[(low.index(ch) + n) % 26]
        else:
            ans += " "
    return ans


s = "AB"
s = "z"
n = 1
print(solution(s, n))
