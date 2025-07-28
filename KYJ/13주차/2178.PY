from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    queue=deque()
    queue.append((0,0))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx <0 or nx>=n or ny <0 or ny>=m:
                continue
            if arr[nx][ny]==1:
                queue.append((nx,ny))
                arr[nx][ny]=arr[x][y]+1

    return arr[n-1][m-1]

print(bfs(0,0))