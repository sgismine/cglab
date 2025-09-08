import sys
from collections import deque

n,m=map (int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b]+=1

q=deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

answer = []


while q:
    pop=q.popleft()
    answer.append(pop)

    for new in graph[pop]:
        indegree[new]-=1
        if indegree[new] == 0:
            q.append(new)


for i in range(n):
    print(answer[i],end=' ')
