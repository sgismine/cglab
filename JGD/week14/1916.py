# 다익스트라 알고리즘
# 18352번과는 거리 사이 비용이 0 or 1 -> deque를 쓰면 최단 경로는 찾아지지만, 최소 비용은 찾을수 x
# 우선순위큐를 사용해야함

import sys
import heapq
input = sys.stdin.readline
INF = 1e8

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가

for _ in range(m):
    u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
    graph[u].append((v, w))

start, end = map(int,input().split())
distance = [INF] * (n+1) # 거리 초기화

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #(비용,출발노드)로 들어감
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 비용이 가장 적은 값이 pop

        if distance[now] < dist: # 이미 더 짧은 경로로 현재 위치를 방문한 적이 있으면 무시
            continue

        for next,cost in graph[now]: # 현 위치에서 갈 수 있는 모든 노드와 비용 확인
            new_cost = dist + cost
            if new_cost < distance[next]: #새로운 거리 정보가 기존 거리 정보보다 작다면 갱신해야함
                distance[next] = new_cost
                heapq.heappush(q,(new_cost,next))

dijkstra(start)
print(distance[end])

