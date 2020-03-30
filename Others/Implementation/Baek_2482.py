"""
    @ Baek 2482 색상환
    @ Prob. https://www.acmicpc.net/problem/2482
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

def NCK(n, k):
    numerator = 1
    denominator = 1
    k = min(n-k, k)
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i
    return numerator/denominator


mod = 1000000003
N = int(input())
K = int(input())
res = 0

trp = 0
for i in range(K):
    NCK(N-trp, K)



