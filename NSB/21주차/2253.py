# 2253 점프
# 개인적으로 점화식 찾기가 어려워 BFS 방법이 편한 것 같습니다.

import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int,input().split())
check = [[] for _ in range(N + 1)]
ss = set()
for _ in range(M):
    s = int(input())
    ss.add(s)


def solution(N, check, ss):
    queue = deque([(1, 0, 0)])
    while queue:
        location, jump, n = queue.popleft()
        for x in [jump + 1, jump, jump - 1]:
            if x > 0:
                next_location = location + x
                if next_location == N:
                    return n + 1
                if (
                    next_location < N
                    and next_location not in ss
                    and x not in check[next_location]
                ):
                    check[next_location].append(x)
                    queue.append((next_location, x, n + 1))
    return -1


print(solution(N, check, ss))
