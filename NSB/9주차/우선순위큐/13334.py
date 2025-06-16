# 13334 철로
# 하나도 이해 안돼서 담주까지 공부해갈게요..
import sys
import heapq
input = sys.stdin.readline

n = int(input())

office = []

for _ in range(n):
    start, end = map(int,input().split())
    if start >= end:
        start, end = end, start
    heapq.heappush(office, (end,start))

d = int(input())

possible = []
res = 0
cnt = 0
while office:
    end, start = heapq.heappop(office)
    if start >= end - d:
        heapq.heappush(possible,(start, end))
        cnt += 1
    while possible:
        s, e = heapq.heappop(possible)
        if s < end -d:
            cnt -= 1
        else:
            heapq.heappush(possible,(s,e))
            break
    res = max(res,cnt)

print(res)
