"""
    @ Baek 5566 주사위 게임
    @ Prob. https://www.acmicpc.net/problem/5566
      Ref.
      Ref Prob.
    @ Algo: 구현(시뮬레이션)
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

N, M = map(int, input().split())
MAP = []
loc = 0
for _ in range(N):
    MAP.append(int(input()))

cnt = 0
for _ in range(M):
    x = int(input())
    cnt += 1
    loc += x
    if loc >= N:
        break
    loc += MAP[loc]
    if loc >= N:
        break

    
# print("cnt", cnt)
print(cnt)


"""
10 5
0
0
5
6
-3
8
1
8
-4
0
1
3
5
1
5
>>>>>>>>>
5
"""