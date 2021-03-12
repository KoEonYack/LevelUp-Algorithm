"""
    @ 42839. 소수찾기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42839
     Ref.   https://geonlee.tistory.com/115
    @ Algo: Brute force
    @ Start day: 20. 03. 02.
    @ End day: 20. 03. 02
"""

from itertools import permutations


def solution(n):
    # a라는 집합을 선언
    a = set()

    # list나 set은 매개변수로 map()를 줄 수 있다.
    # ex. x = ['1','2','3']
    # x = set(map(int, x))
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))

    # a에는 부분집합들이 담겨있다.
    # 소수가 아닌 0-1은 제외
    a -= set(range(0, 2))

    #print(a)
    # {32, 2, 3, 321, 132, 231, 12, 13, 21, 213, 23, 312, 123, 31}

    # 소수 구하는 식
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

print(solution("17"))      # 3
#print(solution("1234567")) # 3