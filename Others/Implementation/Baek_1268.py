"""
    @ Baek 14918 임시 반장 정하기
    @ Prob. https://www.acmicpc.net/problem/14918
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 06. 18.
    @ End day: 20. 06. 18.
"""

MAP = []
N = int(input())
ST = [0] * (N+1)
cacheST = [[] for _ in range(N+1)]
for i in range(N):
    MAP.append(list(input().split()))

for i in range(5):
    for j in range(N):
        for k in range(N):
            if j != k and MAP[j][i] == MAP[k][i]:
                # if j+1 == 4:
                #     print(j, i, k, i)
                if k+1 not in cacheST[j+1]:
                    cacheST[j+1].append(k+1)
                    ST[j+1] += 1

# print(ST)

ch = -1
idx = -1
for i in range(1, len(ST)):
    if ch < ST[i]:
        ch = ST[i]
        idx = i

print(idx)

"""
5
2 3 1 7 3
4 1 9 6 8
5 5 2 4 4
6 5 2 6 7
8 4 2 2 2
>
4
"""