"""
    @ Baek 1359 복권
    @ Prob. https://www.acmicpc.net/problem/1359
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 06. 11.
    @ End day: 20. 06. 11.
"""

# N = 100000
N = 10
DP = [1] * (N+1)

def factorial():
    for i in range(2, N+1):
        DP[i] = DP[i-1] * i

factorial()
print(DP[3])

"""
3 1 1
>
0.3333333333333333
"""