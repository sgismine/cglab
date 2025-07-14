# 1707 이분그래프
import sys
input = sys.stdin.readline

def dfs(start, group):

    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            a = dfs(i,-group)
            if not a:
                return False
        elif visited[start] == visited[i]:
            return False
    return True

k = int(input())
for _ in range(k):
    V,E = map(int,input().split())
    graph = [[] for i in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if not visited[i]:
            result = dfs(i,1)
            if not result:
                break
    print("YES" if result else "NO")

