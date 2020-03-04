"""
    @ Baek 2525 오븐 시계
    @ Prob. https://www.acmicpc.net/problem/2525
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 04.
    @ End day: 20. 03. 04.
"""

H, M = map(int, input().split())
input_M = int(input())

M += input_M
H += M // 60
print(H % 24, M % 60)


"""
14 30
20
>
14 50
"""