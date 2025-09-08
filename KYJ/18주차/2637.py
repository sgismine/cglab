import sys 
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
need=[[0]*(n+1) for _ in range(n+1)]
q=deque()
degree=[0]*(n+1)

for _ in range(1,m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[b].append((a,c))
    degree[a]+=1

for i in range(1,n+1):
    if degree[i]==0:
        q.append(i)


while q:
    now=q.popleft()
    for next,amount in graph[now]:
        if need[now].count(0)==n+1:
            need[next][now]+=amount
        else:
            for i in range(1,n+1):
                need[next][i] += need[now][i] * amount

        degree[next]-=1
        if degree[next]==0:
            q.append(next)

for parts in enumerate(need[n]):
    if parts[1]>0:
        print(parts[0],parts[1])


