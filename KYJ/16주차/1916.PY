import sys
import heapq

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start,end=map(int,sys.stdin.readline().split())


distance=[int(1e9)]*(n+1)

def dij(node):
    queue=[]
    heapq.heappush(queue,(0,node))
    distance[node]=0

    while queue:
        dist,now=heapq.heappop(queue)
        if distance[now]<dist:
            continue

        for i in graph[now]:
            weight=dist+i[1]
            if weight < distance[i[0]]:
                distance[i[0]]=weight
                heapq.heappush(queue,(weight,i[0]))

dij(start)
print(distance[end])

