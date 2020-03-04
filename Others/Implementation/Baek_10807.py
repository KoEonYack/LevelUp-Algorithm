"""
    @ Baek 10807 개수 세기
    @ Prob. https://www.acmicpc.net/problem/10807
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

N = int(input())
arr = list(map(int, input().split()))
v = int(input())
print(arr.count(v))

"""
11
1 4 1 2 4 2 4 2 3 4 4
2
>
3
"""