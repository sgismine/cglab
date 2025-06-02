# 1, 2, 3, 4, 5, 6, 7
# 세 번째 숫자 삭제하고 그 자리에서 다시 3번째로 감


from collections import deque

def cycle(N, K):
   
    queue = deque(range(1, N + 1))        # 1~ N 숫자 생성하고 deaue로 큐에 저장 
                      

    
    while queue:                          # 큐에 숫자가 남아 있는 동안만 반복 -> 없으면 탈
        for i in range(K-1) :             # K = 3이면 1, 2까지 뽑아서 뒤로 보내기
            queue.append(queue.popleft())  
        print(queue.popleft())                   # 제일 앞에 3 출력 
    


N, K = map(int, input().split())
cycle(N, K)

### 출력 형식오류


from collections import deque

def cycle(N, K):
    queue = deque(range(1, N + 1))  
    result = []  

    while queue:  
        for i in range(K-1): 
            queue.append(queue.popleft())
        result.append(queue.popleft())  
    
    #출력형식 포맷
    print(f"<{', '.join(map(str, result))}>")

N, K = map(int, input().split())
cycle(N, K)
