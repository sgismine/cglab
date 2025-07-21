import sys
sys.setrecursionlimit(10**6) #노드의 개수 N (2 ≤ N ≤ 100,000)
input = sys.stdin.readline

# 입력 처리
n = int(input())
graph = []  

for i in range(n + 1): #1번부터 시작하니까 n+1까지로 설정
    graph.append([]) 


for _ in range(n - 1): #트리에서 노드 개수 n개임
    a, b = map(int, input().split())
    graph[a].append(b) #양방향 연결
    graph[b].append(a)


parent = [0] * (n + 1) #0번째 노드 안쓸거임 버림 
visited = [False] * (n + 1) #같은 이슈

# DFS 함수 정의
def dfs(current):
    visited[current] = True 
    for neighbor in graph[current]:
        if not visited[neighbor]:
            parent[neighbor] = current  
            dfs(neighbor)   #다음 이웃 탐색 ㄱㄱ

# 루트를 1로 정하고 시작 (문제)
dfs(1)

# 결과 출력
for i in range(2, n + 1): #문제 에서 2번노드 부모부터 출력하라함
    print(parent[i])
