import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 부품 개수 (N은 완제품 번호)
M = int(input())  # 관계 개수

graph = [[] for _ in range(N + 1)]   # 부품 u를 사용해서 만들 수 있는 부품들
indegree = [0] * (N + 1)             # 진입차수 : x를 만들기 전에 먼저 만들어져야하는 부픔 개수 

# 관계 입력
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # Y -> X (X 만들려면 Y 필요)
    indegree[X] += 1

# DP 테이블: need[x][i] = x를 만들 때 필요한 기본부품 i 개수
need = [[0] * (N + 1) for _ in range(N + 1)] #세팅

queue = deque()

# 진입 차수 0인 건 기본 부품
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        need[i][i] = 1  # 자기 자신을 만들 때 자기 1개 필요

# 위상 정렬
while queue:
    now = queue.popleft() #DLAL RLQHS QNVNADLA

    for nxt, k in graph[now]:
        # now 부품이 nxt를 만드는데 k개 필요하다
        for i in range(1, N + 1):
            need[nxt][i] += need[now][i] * k
            
        indegree[nxt] -= 1
        
        if indegree[nxt] == 0:
            queue.append(nxt)

# 출력: 완제품 N을 만들기 위한 기본 부품 개수
for i in range(1, N):
    if need[N][i] > 0:
        print(i, need[N][i])
