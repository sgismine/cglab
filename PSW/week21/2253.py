import sys

# 입력 속도 빠르게 하기
input = sys.stdin.readline

# 돌의 개수 n, 밟을 수 없는 돌의 개수 m
n, m = map(int, input().split())

# 못 밟는 돌 번호를 저장할 집합
stone = set(int(input()) for _ in range(m))

# DP 테이블 초기화
# jump[i][x] = i번 돌에 '직전 점프 거리 x'로 도착했을 때 최소 점프 횟수
# 모든 값을 INF(1e9)로 초기화
max_speed = int((2 * n) ** 0.5) + 1  # 점프 속도의 현실적 상한
jump = [[int(1e9)] * max_speed for _ in range(n + 1)]

# 시작점: 1번 돌, 아직 점프 안 함 (speed=0), 점프 횟수 0
jump[1][0] = 0

# 2번 돌부터 N번 돌까지 DP 계산
for i in range(2, n + 1):
    # 밟을 수 없는 돌이면 건너뜀
    if i in stone:
        continue

    # 가능한 점프 거리 x 범위: 1 ~ sqrt(2*i)
    for x in range(1, int((2 * i) ** 0.5) + 1):
        # 이전 위치는 i - x
        # 그 위치에서 가능한 점프 속도는 x-1, x, x+1
        # 이전 세 가지 속도의 최소 점프 횟수 중 하나 + 1이 현재 점프 횟수
        jump[i][x] = min(jump[i - x][x - 1:x + 2]) + 1

# N번 돌에 도달 가능한 점프 거리 중 최소값
answer = min(jump[n])

# 도달 불가능이면 -1, 아니면 최소 점프 횟수 출력
print(-1 if answer == int(1e9) else answer)
