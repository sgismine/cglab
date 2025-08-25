import sys
from collections import deque
m,n,h=map(int,sys.stdin.readline().split())
graph=[[list(map(int,sys.stdin.readline().split()))for _ in range(n)]for _ in range(h)]

dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]
queue=deque()

def bfs():
    while queue:
        z,x,y=queue.popleft()
        for i in range(6):
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny]==0:
                    graph[nz][nx][ny]=graph[z][x][y]+1
                    queue.append((nz,nx,ny))


for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y]==1:
                queue.append((z,x,y))

bfs()
day=0
success=True
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y]==0:
                print(-1)
                sys.exit(0)
            day=max(day,graph[z][x][y])


print(day-1)