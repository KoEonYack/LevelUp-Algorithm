"""
    @ 프로그래머스 : 나누어 떨어지는 숫자 배열
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12910
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(arr, divisor):
    return sorted([num for num in arr if num % divisor == 0]) or [-1]

arr = [5, 9, 7, 10]
arr = [3, 2, 6]
divisor	= 5
divisor = 10
print(solution(arr, divisor))