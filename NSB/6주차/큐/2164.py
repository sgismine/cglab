# 2164 카드2 1번

# 이거 시간 초과 뜨네요..
# N = int(input())
# queue = list(range(1,N+1))

# while(len(queue)>1):
#     queue.pop(0)
#     queue.append(queue.pop(0))
# print(queue[0])

# deque쓰라고 하는데 -> 왼쪽값 뺄때는 deque가 빠름
# from collections import deque
# N = int(input())
# cards = deque([i for i in range(1,N+1)])
# while len(cards) > 1 :
#     cards.popleft()
#     cards.append(cards.popleft())
# print(cards[0])

# 요세푸스 문제라고 하네요... 공식 찾아서 푸는건데 시간 엄청 빠름
N = int(input())
square = 2
while True:
    if(N == 1 or N == 2):
        print(N)
        break
    square *= 2
    if(square >= N):
        print((N-(square // 2)) * 2)
        break