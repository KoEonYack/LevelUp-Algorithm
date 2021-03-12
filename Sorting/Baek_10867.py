"""
    @ Baek 10867 중복 빼고 정렬하기
    @ Prob. https://www.acmicpc.net/problem/10867
      Ref.
      Ref Prob.
    @ Algo: Sort
    @ Start day: 20. 03. 09.
    @ End day:  20. 03. 09.
"""

N = int(input())
arr = list(map(int, input().split()))
arr = set(arr)
arr = list(arr)
arr.sort()
print(*arr)

"""
10
1 4 2 3 1 4 2 3 1 2
>
1 2 3 4
"""