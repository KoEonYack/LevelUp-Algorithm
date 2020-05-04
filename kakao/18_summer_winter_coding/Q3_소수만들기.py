"""
    @ 18 Summer winter coding: 소수 만들기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12977
      Ref.
      Ref Prob.
    @ Algo:
    @ Start day: 20. 05. 04.
    @ End day: 20. 05. 04.
"""

def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

def solution(nums):
    answer = 0
    N = len(nums)

    for i in range(0, N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                total_num = nums[i] + nums[j] + nums[k]
                if isPrime(total_num):
                    answer += 1

    return answer

print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 1