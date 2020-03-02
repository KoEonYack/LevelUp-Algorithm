"""
    @ Prog 42746 가장 큰 수
    @ Prob. https://www.acmicpc.net/problem/42746
      Ref.  https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98-in-python
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 03. 02.
    @ End day: 20. 03. 02.
"""


def solution(numbers):
    num_arr = [str(i) for i in numbers]
    num_arr.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(num_arr)))


print(solution([6, 10, 2])) # 6210
print(solution([3, 30, 34, 5, 9]))
# 9534330
# 9534330

print("3" < "30" )
print("3" * 3 < "30" * 3)