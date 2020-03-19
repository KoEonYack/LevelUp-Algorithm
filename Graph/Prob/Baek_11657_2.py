from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
q=deque([(sx-1,sy-1)])
t=[0,0]
if D[ex-1][ey-1]=='X': t[0]=1
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if nx==ex-1 and ny==ey-1:
                if t[0]==1: t[1]=1
                else:
                    t[0]=1
                    q.append((nx,ny))
            elif D[nx][ny]!='X':
                q.append((nx,ny))
                D[nx][ny]='X'
print(['NO','YES'][t[1]==1])

"""
5 4
.X..
...X
X.X.
....
.XX.
5 3
1 1
>
NO
"""