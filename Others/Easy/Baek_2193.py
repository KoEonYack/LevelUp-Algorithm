"""
    @ Baek 2193 이친수 ??
    @ Prob. https://www.acmicpc.net/problem/2193
      Ref.
      Ref Prob.
    @ Algo: 구현(수학)
    @ Start day: 20. 01. 06
    @ End day: 20. 01. 06
"""


N = int(input())


N = pow(2, N)
binNum = bin(N)
if binNum[2] is not 0 and "11" not in binNum:
    print(binNum)

"""
3 (0b11)
>
2
"""