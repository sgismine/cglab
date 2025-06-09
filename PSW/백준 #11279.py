#heapq.heappush(heap, item)
#이 함수는 아이템을 힙에 추가

#heapq.heappop(heap)
#힙에서 가장 작은 아이템을 뺴고 그 값을 반한 
#이 함수 자체가 값을 반환하기 때문에 print를 쓰면 값을 출력할 수 있음

#heapq.heappushpop(heap, item)
#아이템을 힙에 추가한 다음, 가장 작은 아이템을 빼고 그 값을 반환

#heapq.heapify(x)
#리스트 x를 즉각적으로 heap으로 변환 > (O(N))

#heap은 최소힙 기준 !!!!!!!!!
# 최대힙 만드려면 음수로 값 두 개 저장


import sys
import heapq

n = int(sys.stdin.readline())
heap = []                      #힙 배열 만들어두기

for _ in range(n) :             #반복 변수의 의미를 두지 않음 !!!!!!
    val = int(sys.stdin.readline())
    
    if(val == 0):
        if(len(heap) == 0):    #힙이 비어있다면 0출력
            print(0)
        else:
            print(heapq.heappop(heap)[1]) # 아니면 힙에서 가장 큰 값을 제거 및 반환하고 그 값을 출력
                                          # heapq.heappop(heap)[1]은 반환된 튜플에서 두 번째 요소(원래 값)만 추출  ex) (-3,3) 에서 3꺼냄
    else:
        heapq.heappush(heap,(-val,val))   #입력값이 0이 아닌 경우: heapq.heappush를 사용해 힙에 (음수 값, 원래 값) 형태로 추가
                                          #이렇게 하면, heapq는 음수 값을 기준으로 정렬하여 최대 힙처럼 동작하게 됩니다.


