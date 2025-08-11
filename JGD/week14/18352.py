import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = {}

for i in range(n+1):
    graph [i] = []

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)


def bfs(x):
    queue = deque()
    queue.append(x)

    dist = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    visited[x] = 1

    while(queue):
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                dist[i] = dist[node]+1

    return dist

result = bfs(x)

cnt = 0
for idx,val in enumerate(result):
    if val == k:
        print(idx)
        cnt+=1
if not cnt:
    print(-1)