'''
    @ [Level 2] K번째 수 - Fail
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42748
      Ref.
    @ Algo: Sorting
    @ Start day: 19. 09. 06
    @ End day:
'''

def solution(citations):
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i


print(solution([3, 0, 6, 1, 5]))
