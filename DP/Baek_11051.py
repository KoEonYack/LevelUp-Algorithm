"""
    @ Baek 11051. 이항 계수 2
    @ Prob. https://www.acmicpc.net/problem/11051
     Ref.
    @ Algo: DP
    @ Start day: 20. 04. 12.
    @ End day: 20. 04. 12.
"""

N, K = map(int, input().split())
DP = [[0]*1 for _ in range(1002)]
DP[1].append(1)
for i in range(2, 1002):
    for j in range(1, i+1):
        if j == 1:  # 한 줄의 시작
            DP[i].append(1)
        elif j == i: # 한 줄의 끝
            DP[i].append(1)
        else:
            DP[i].append(DP[i-1][j-1] + DP[i-1][j])

print(DP[N+1][K+1] % 10007)


# for a in DP:
#     print(a)

"""
5 2
>
10
"""
