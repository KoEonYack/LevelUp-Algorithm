"""
    @ Baek 2417 정수 제곱근
    @ Prob. https://www.acmicpc.net/problem/2417
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

N = int(input())
if pow(N, 1/2) < N:
    print(int(pow(N, 1/2))+1)
else:
    print(int(pow(N, 1/2)))


"""
122333444455555
>
11060446
"""

