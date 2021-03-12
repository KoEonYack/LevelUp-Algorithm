def FloodFill():
    q.append((i,j))
    check[i][j]=1
    t=1
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]==D[x][y] and check[nx][ny]==0:
                check[nx][ny]=1
                q.append((nx,ny))
                t+=1
    return t
from collections import deque
m,n=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
check=[[0]*m for _ in range(n)]
q=deque()
B,W=0,0
dx,dy=[1,-1,0,0],[0,0,1,-1]
for i in range(n):
    for j in range(m):
        if check[i][j]==0:
            ans = FloodFill()
            print(ans)
            if D[i][j]=='W': W+=ans**2
            else: B+=ans**2
print(W,B)

"""
5 3
WBWWW
WWWWW
WWWWW
"""
