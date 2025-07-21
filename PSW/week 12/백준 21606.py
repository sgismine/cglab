import sys
sys.setrecursionlimit(10**6)

n = int(input()) 
A = input().strip()  # 실내 1 실외 0 strip는 공백제거
graph = [[] for _ in range(n)]  # 0 ~ n-1

# 트리의 간선 정보를 입력받아 그래프에 저장
for _ in range(n - 1):
    u, v = map(int, input().split())  
    u -= 1  # 인덱스 0부터 시작
    v -= 1
    graph[u].append(v) # 양쪽으로 추가 -> 트리 양방향
    graph[v].append(u)

visited = [False] * n  # 방문한 정점 표시 -> dfs사용
answer = 0  


def dfs(node):
    visited[node] = True  
    cnt = 0                       # 실내노드 수
    for neighbor in graph[node]:  
        if not visited[neighbor] and A[neighbor] == '0':  # 방문안함 + 실외 -> 계속 탐색
            cnt += dfs(neighbor)                          # 재귀탐색 -> 연결된 실내 개수 더하기
        elif A[neighbor] == '1':  # 이웃이 실내다 
            cnt += 1
    return cnt

# 실내 - 실내
for u in range(n):
    if A[u] == '1':         
        for v in graph[u]:  
            if A[v] == '1':  # 이웃도 실내면
                answer += 1  # 실내-실내 직접 연결 경로 +1 

# 중복방지 
answer //= 2

# 실외로 나가는 경우
for i in range(n):
    if A[i] == '0' and not visited[i]:  # 방문 안 한 실외 노드
        cnt = dfs(i)                    # 연결된 실내 노드 수 -> dfs돌려서 구하김
        answer += cnt * (cnt - 1) // 2  

# 정답 출력
print(answer)
