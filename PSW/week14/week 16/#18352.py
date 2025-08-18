from collections import deque
import sys

# 입력
n, m, k, x = map(int, sys.stdin.readline().split())

# 그래프 
graph = {} #딕셔너리
for i in range(n+1):
    graph[i] = []
    
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# BFS 준비
distance = [0 for _ in range(n + 1)]   # 최단거리 저장
visited = [0 for _ in range(n + 1)]    # 방문 여부
queue = deque([x])

visited[x] = 1   # 시작 도시는 방문 처리
while queue:
    current_city = queue.popleft()   # 지금 탐색 중인 도시
    for next_city in graph[current_city]:
        if visited[next_city] == 0:             # 아직 방문 안 했다면
            queue.append(next_city)             # 큐에 넣고
            visited[next_city] = 1              # 방문 처리
            distance[next_city] = distance[current_city] + 1  # 최단거리 기록

# 결과 출력
found = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        found += 1

if found == 0:
    print(-1)
