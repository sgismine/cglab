import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인접 리스트
indegree = [0] * (N + 1)  # 진입 차수

# 간선 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)                # A가 B앞에 서야 하므로 간선  A -> B 추가
    indegree[B] += 1                 # 집입차수 1 추가해줘야함 나중에 1씩 뺌

# 위상 정렬 (큐 이용)
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:            # 진입차수 0이면 큐에 추가
        queue.append(i)

result = []

while queue:
    now = queue.popleft()         # 왼쪽 부터 POP하기 먼저 큐에 추가 된순
    result.append(now)            # 큐에서 꺼낸 애들 

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(" ".join(map(str, result))) #result 리스트여서 공백기분으로 꺼내서 출력
