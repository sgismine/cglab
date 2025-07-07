import sys
import heapq
#프림알고리즘

V,E=map(int,sys.stdin.readline().split())

arr=[[] for _ in range(V)]
for _ in range(E):
    v1,v2,d=map(int,sys.stdin.readline().split())
    arr[v1-1].append([v2-1,d])
    arr[v2-1].append([v1-1,d])


que,dist,cnt=[],0,0 #que:우선순위 큐,dist:총가중치,cnt=방문한 정점개수
visit=[False for _ in range(V)]
heapq.heappush(que,(0,0)) #(거리,정점)

while cnt <V:
    (d,v3)=heapq.heappop(que)
    if not visit[v3]:
        visit[v3]=True
        dist = dist+d
        cnt = cnt+1

        for e in arr[v3]:
            if not visit[e[0]]:
                heapq.heappush(que,(e[1],e[0]))

print(dist)