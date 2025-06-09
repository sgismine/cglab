import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []
heapq.heapify(heap)


for i in range(n):
    x = int(input())
    
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            max = heapq.heappop(heap)[1]
            print(max)
    else:
        heapq.heappush(heap,(-x,x))