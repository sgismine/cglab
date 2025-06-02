# 큐 -> FIFO 선입선출
# 파이썬 큐 구현 방법  collections 모듈 deque 사용하기
# deque는 list에는 없는 popleft()라는 메서드를 제공
   # 이 메서드를 사용하면 첫 번째 데이터를 제거할 수 있다.
   # queue & deque 개념 url
   # https://www.daleseo.com/python-queue/ 





from collections import deque

def last_Number(N):
  
    queue = deque(range(1, N + 1))    # 1~ N 숫자 생성하고 deaue로 큐에 저장 
                                      # N = 4 라면 deque([1, 2, 3, 4])

   
    while len(queue) > 1:             # queue에 카드가 한 장 남을 때 까지 반복
        
        queue.popleft()               # 제일 앞에 있는 카드 (1) 제거 
                                      # deaue([2, 3, 4])
        
        queue.append(queue.popleft()) # 제일 앞에 있는 카드 (2) 를 제일 뒤에서 append하기 
        
                                      # 이 루프를 한장 남을 때까지 반복하고 한 장 남으면
    

    return queue[0]                   # 한 장 남은 queue 반환


N = int(input())
print(last_Number(N))


# 우선순위 큐 공부하다 풀어서  우선순위로 풀어보려다가 카드 맨뒤로 보내는거 몰라서 버림


# from queue import PriorityQueue

# def last_Number(N):
    
#     queue = PriorityQueue()
#     for i in range(1, N + 1):
#         queue.put((i, i))           # (우선순위, 값) 추가

#     while queue.qsize() > 1:
        
#         queue.get()                 # 가장 위의 카드를 버림
       