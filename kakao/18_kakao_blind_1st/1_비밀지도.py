"""
    @ 18 kako blind: 비밀지도
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/17681
      Ref.
      Ref Prob.
    @ Algo: 구현(bin)
    @ Start day: 20. 05. 05.
    @ End day: 20. 05. 05.
"""


def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        ans.append(("0" *(n - len(bin_str)) + bin_str).replace("1", "#")
                                                      .replace("0", " "))
    return ans


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
#["#####","# # #", "### #", "# ##", "#####"]


