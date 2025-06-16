# 1260 DFS와 BFS

from collections import deque

# 깊이우선탐색 dfs
def dfs(v):
    print(v, end=' ')
    visited1[v] = True
    for i in range(1, n+1):
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)

# 너비우선 탐색 bfs
def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i] == 1:
                q.append(i)
                visited2[i] = True

# 입력 및 그래프 2차원 배열로 그리기
n, m, v = map(int,input().split())
graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
# 방문 여부 리스트
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

dfs(v)
print()
bfs(v)
