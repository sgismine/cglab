# 2098 외판원순회
# 진짜 풀어볼 엄두도 안나는 문제

# 재귀함수(시간초과)
# DFS로 최단 경로 탐색 후 DP 점화식을 사용하여 최소비용 탐색

# import sys

# input = sys.stdin.readline

# n = int(input())

# INF = int(1e9)
# dp = [[INF] * (1<<n) for _ in range(n)]
# graph = []


# def dfs(x, visited):
#     if visited == (1<<n) -1:
#         if graph[x][0]:
#             return graph[x][0]
#         else:
#             return INF
        
#     if dp[x][visited] != INF:
#         return dp[x][visited]
    
#     for i in range(1,n):
#         if not graph[x][i]:
#             continue
#         if visited & (1<<i):
#             continue
        
#         # 점화식 부분
#         dp[x][visited] = min(dp[x][visited],dfs(i,visited | (1<<i)) + graph[x][i])
#     return dp[x][visited]
    
# for i in range(n):
#         graph.append(list(map(int,input().split())))
        
# print(dfs(0,1))


# 반복문
# 재귀함수를 사용하지 않고 반복문을 사용

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp = [[INF] * (1<<n) for _ in range(n)]
dp[0][1] = 0

for visited in range(1<<n):
    for x in range(n):
        if dp[x][visited] == INF:
            continue
        for nxt in range(n):
            if not graph[x][nxt] or (visited & (1<<nxt)):
                continue
            dp[nxt][visited | (1<<nxt)] = min(
                dp[nxt][visited | (1<<nxt)],
                dp[x][visited] + graph[x][nxt]
            )

ans = INF
for i in range(n):
    if graph[i][0]:
        ans = min(ans, dp[i][(1<<n)-1] + graph[i][0])

print(ans)
