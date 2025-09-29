# 2098 외판원순회
# 진짜 풀어볼 엄두도 안나네요... 자료많이 참고함

import sys

input = sys.stdin.readline

n = int(input())

INF = int(1e9)
dp = [[INF] * (1<<n) for _ in range(n)]
graph = []


def dfs(x, visited):
    if visited == (1<<n) -1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF
        
    if dp[x][visited] != INF:
        return dp[x][visited]
    
    for i in range(1,n):
        if not graph[x][i]:
            continue
        if visited & (1<<i):
            continue
        
        # 점화식 부분
        dp[x][visited] = min(dp[x][visited],dfs(i,visited | (1<<i)) + graph[x][i])
    return dp[x][visited]
    
for i in range(n):
        graph.append(list(map(int,input().split())))
        
print(dfs(0,1))