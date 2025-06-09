import sys
import heapq

# 최소힙 : 부모노드가 자식 노드보다 작은 값을 가지는 완전이진트리 -> 최소값에 바로 접근
# 최대힙 : 부모노드가 자식 노드보다 큰 값을 가지는 완전 이진트리 -> 최대값에 바로 접근


input = sys.stdin.readline
n = int(input())
max_heap = []
min_heap = []

for i in range(n):
    tmp = int(input())

    # 중앙값보다 작은 값은 Max heap에, 중앙값보다 큰 값은 Min heap에 저장
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-tmp) # 최대힙은 음수로 바꿔서(heapq는 최소힙만 지원)
    else:
        heapq.heappush(min_heap,tmp)

    # min_heap의 root값이 max_heap의 root값 보다 작다면 두 수를 바꿔줌
    if min_heap and -max_heap[0] > min_heap[0]:
        temp_min = heapq.heappop(min_heap)
        temp_max = heapq.heappop(max_heap)
        heapq.heappush(max_heap, -temp_min)
        heapq.heappush(min_heap, -temp_max)
    
    

    # print("min_heap = ",min_heap)
    # print("max_heap = ",max_heap)
    # print("median = ",-max_heap[0])

    print(-max_heap[0])
    

