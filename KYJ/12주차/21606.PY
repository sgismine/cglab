import sys
sys.setrecursionlimit(10**5)

n=int(sys.stdin.readline())
A=sys.stdin.readline().rstrip()

graph=[[] for _ in range(n+1)]
place=[0]*(n+1)
visited=[0]*(n+1)


for i in range(len(A)):
    if A[i]=='1':
        place[i+1]=1

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    res = 0 
    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                res += dfs(next_node)
        else:
            res += 1
    return res

ans = 0
for i in range(1, n+1):
    if place[i] == 0: #실내->실외->실내
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res - 1) #조합 
    else: #실내->실내
        for next_node in graph[i]: 
            if place[next_node] == 1:
                ans += 1
print(ans)