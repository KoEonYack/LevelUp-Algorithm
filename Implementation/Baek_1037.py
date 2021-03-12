"""
    @ Baek 1037 약수
    @ Prob. https://www.acmicpc.net/problem/1037
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 06.
    @ End day: 20. 03. 06.
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[0] * arr[-1])

"""
2
4 2
>
8
"""
