"""
    @ 프로그래머스 : 문자열 내 마음대로 정렬하기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12915
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x:(x[n]))
    return strings

def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])