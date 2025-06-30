from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    result.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result

# 입력 받기
n, m, v = map(int, input().split())  # 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n + 1)]  # 인접 리스트로 그래프 구현

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬 (작은 번호 우선 방문을 위해)
for neighbors in graph:
    neighbors.sort()

# DFS 수행
visited_dfs = [False] * (n + 1)
result = []
dfs(graph, v, visited_dfs)
print(*result)

# BFS 수행
result = bfs(graph, v)
print(*result)
