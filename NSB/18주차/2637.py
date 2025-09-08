import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
res = [0]*(n+1)
for _ in range(m):
    x,y,k = map(int,input().split())
    graph[x].append((y,k))
    indegree[y]+=1
    res[n] = 1
    origin = []
    def topological_sort():
        queue = deque([n])
        for i in range(1,n+1):
            if not graph[i]: origin.append(i)
        while queue:
            popnum = queue.popleft()
            for part,count in graph[popnum]:
                res[part]+=count*res[popnum]
                
                indegree[part]-=1
                if indegree[part]==0:
                    queue.append(part)
topological_sort()
for i in origin:
    print(i, res[i])
    