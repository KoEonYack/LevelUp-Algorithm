"""
    @ Baek 11048 이동하기
    @ Prob. https://www.acmicpc.net/problem/11048
      Ref.  
    @ Algo: 
    @ Start day: 20. 09. 04.
    @ End day: 20. 09. 04.
"""

# N: 세로 M:가로
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + arr[i-1][j-1]

print(DP[-1][-1])



"""
3 4
1 2 3 4
0 0 0 5
9 8 7 6
>
31
----------

3 3
1 0 0
0 1 0
0 0 1
>
3

4 3
1 2 3
6 5 4
7 8 9
12 11 10
>
47

"""