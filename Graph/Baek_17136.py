"""
    @ Back 17136. 색종이 붙이기
    @ Prob. https://www.acmicpc.net/problem/17136
      Ref.  https://daily-life-of-bsh.tistory.com/141
    @ Algo: BFS
    @ Start day: 20. 10. 15.
    @ End day: 20. 10. 15.
"""

import sys

def DFS(r, c, cnt):
    


paper = [0, 5, 5, 5, 5, 5]
ans = sys.maxsize
MAP = [list(input().split(" ")) for _ in range(10)]

for a in MAP:
    print(a)


DFS(0, 0, 0)
print(-1 if ans == sys.maxsize else ans)



"""
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
>
0
"""