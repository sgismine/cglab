import sys
from collections import deque


def bfs(start, group):
    queue = deque([start])  
    visited[start] = group  
    while queue:  

        x = queue.popleft()  

        for i in graph[x]:  
            if not visited[i]:  
                queue.append(i)  
                visited[i] = -1 * visited[x] 
            elif visited[i] == visited[x]:  
                return False  
    return True 

k=int(sys.stdin.readline())


for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]  
    visited = [False] * (V + 1)  

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)  
        graph[b].append(a)  

    for i in range(1, V + 1):
        if not visited[i]:  
            result = bfs(i, 1)
            if not result:
                break

    if result:
        print('YES')
    else:
        print('NO')