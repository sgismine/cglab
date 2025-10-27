import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# dp[current][visited] : 현재 도시 current, 방문 상태 visited 일 때 최소 비용
dp = [[None] * (1 << N) for _ in range(N)]

def tsp(current, visited):
    # 모든 도시 방문 완료
    if visited == (1 << N) - 1:
        return W[current][0] if W[current][0] != 0 else float('inf')

    # 이미 계산한 경우
    if dp[current][visited] is not None:
        return dp[current][visited]

    cost = float('inf')
    for next in range(N):
        if not (visited & (1 << next)) and W[current][next] != 0:
            # next 도시 방문
            cost = min(cost, W[current][next] + tsp(next, visited | (1 << next)))

    dp[current][visited] = cost
    return cost

print(tsp(0, 1))  # 0번 도시에서 출발, 0번 도시 방문 표시 (visited = 1)
