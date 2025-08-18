import sys
from collections import deque

n,m,k,x=map(int,sys.stdin.readline().split())

graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)


distance=[-1]*(n+1)
def bfs(v):
    queue=deque()
    queue.append(v)
    distance[v] = distance[v]+1
    
    while(queue):
        pop = queue.popleft()
        for i in graph[pop]:
            if(distance[i]==-1):
                distance[i]=distance[pop]+1
                queue.append(i)

bfs(x)

if(k in distance):
    for i in range(1,n+1):
        if(distance[i]==k):
            print(i)

else:
    print(-1)