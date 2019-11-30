'''
    Part2 - Prob1. Find appropriate url

    [Condition]
    Start: only start www.
    Middle: only english and number
    :ast: .com, .net, .edu only

    Check.
        Visualize Reg.
        https://regexper.com/#%5Ewww.
'''
import re

def solution(urls):
    answer = 0

    pattern = re.compile(r'^www\.[a-zA-Z0-9]+(\.com|\.net)$')

    for url in urls:
        if pattern.match(url) is not None:
            answer += 1

    return answer

print(solution(["www.google.com", "www.kakao.com", "ww.....2222"]))