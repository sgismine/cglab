import sys
import heapq


n = int(input())
lst = [] #좌표목록
for i in range(n):
    h,o = map(int,input().split())
    lst.append(min(h,o),max(h,o)) # 집,사무실 위치 상관없이 좌표 크기 순으로

d = int(input())

# 철로를 고려할때 좌표의 시작점이 아닌 끝점을 기준으로 고려
# 철로의 끝점만 고려하면, 힙에 들어와있는 사람은 이미 끝점이 안에 들어와있으므로
# 시작점이 철로 범위 내냐 아니냐만 따지면 됨.

lst.sort(key=lambda x: (x[1],x[0])) #끝점 기준 정렬

heap =[]
cnt = 0

for l in lst:
    start,end = l
    heapq.heappush(heap,start) # 최소 힙, 루트가 최소값
    line_start = end -d # 현재 사람의 끝 좌표에서 d를 빼면 철로의 시작점
    while heap and heap[0] < line_start: #최소 힙이므로 heap[0]이 최소값
        heapq.heappop(heap)
    cnt = max(cnt,len(heap))

print(cnt)

