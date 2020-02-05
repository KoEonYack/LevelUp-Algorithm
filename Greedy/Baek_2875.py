"""
    @ 2875. 대회 or 인턴
    @ Prob. https://www.acmicpc.net/problem/2975
     Ref.
    @ Algo: DFS
    @ Start day: 20. 01. 26.
    @ End day: 20. 01. 26.
"""

# 여, 남, 조합 수
N, M, K = map(int, input().split())

maxV = 0
while N >= 2 and M >= 1 and N+M >= K + 3:
    N -= 2
    M -= 1
    maxV += 1

print(maxV)


"""
6 3 2
>
2
"""