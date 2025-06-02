import sys

from collections import deque

N = int(sys.stdin.readline())
Q = deque()

for _ in range(N):
    list = sys.stdin.readline().split()    #입력받은 문자열을 공백으로 나누어 리스트로 반환
    
    
    # push X: 정수 X를 큐에 넣는 연산이다.
    if list[0] == 'push':  
        Q.append(int(list[1]))


    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if list[0] == 'pop':                 
        if Q:                         # Q 안에 값이 있을 때
            print(Q.popleft())
        else:
            print(-1)


    #size: 큐에 들어있는 정수의 개수를 출력한다.
    if list[0] == 'size':  
        print(len(Q))
        
        
    #empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    if list[0] == 'empty':
        if Q:
            print('0')
        else:
            print('1') 
            
            
    #front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if list[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
            
            
    #back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if list[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)