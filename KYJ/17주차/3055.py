from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
graph=[list(sys.stdin.readline().strip())for _ in range(n)]
distance=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()

for x in range(n):
    for y in range(m):
        if graph[x][y]=='S':
            queue.append((x,y))
        elif graph[x][y]=='D':
            a,b=x,y


for x in range(n):
    for y in range(m):
        if graph[x][y]=='*':
            queue.append((x,y))


def bfs(a,b):
    while queue:
        x,y=queue.popleft()
        if graph[a][b]=='S':
            return distance[a][b]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0<=ny<m:
                if(graph[nx][ny]=='.'or graph[nx][ny]=='D')and graph[x][y]=='S':
                    graph[nx][ny]='S'
                    distance[nx][ny]=distance[x][y]+1
                    queue.append((nx,ny))
                elif(graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    graph[nx][ny]='*'
                    queue.append((nx,ny))

    return 'KAKTUS'

print(bfs(a,b))