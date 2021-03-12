"""
    @ Baek 2501 약수 구하기
    @ Prob. https://www.acmicpc.net/problem/2501
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 05.
    @ End day: 20. 03. 05.
"""


N, K = map(int, input().split())
for i in range(1, N+1):
    if N % i == 0:
        K -= 1
        if K == 0:
            print(i)
            break
else:
    print(0)

"""
6 3
>
3
"""