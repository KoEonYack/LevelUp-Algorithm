"""
    @ Prog 42747 H-Index
    @ Prob. https://www.acmicpc.net/problem/42747
      Ref. https://stroot.tistory.com/115
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 03. 02.
    @ End day: 20. 03. 02.
"""

def solution(citations):
    ans = 0
    citations.sort()

    for i in range(len(citations)):
        h = len(citations) - i

        if citations[i] >= h:
            ans = h
            break

    return ans

print(solution([3, 0, 6, 1, 5])) #
print(solution([1545, 2, 999, 790, 540, 10, 22])) #
print(solution([7])) #
print(solution([0])) #
