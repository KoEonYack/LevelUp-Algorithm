"""
    @ Baek 1100 하얀 칸
    @ Prob. https://www.acmicpc.net/problem/1100
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

MAP = [list(input()) for _ in range(8)]
ans = 0


for i in range(8):
    for j in range(8):
        if MAP[i][j] == "F" and i % 2 == 0 and j % 2 == 0:
            ans += 1
        if MAP[i][j] == "F" and i % 2 != 0 and j % 2 != 0:
            ans += 1
print(ans)

"""
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.
>
1
"""