# 18258

import sys
from collections import deque

cmd = []
queue = deque([])

N = int(input())
for i in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push" :
        queue.appendleft(cmd[1])
    elif cmd[0] == "pop" :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue.pop())

    elif cmd[0] == "size" :    
        print(len(queue))
    elif cmd[0] == "empty" :    
        if len(queue) == 0 :
            print(1)
        else :
            print(0)

    elif cmd[0] == "front" : 
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[-1])
    elif cmd[0] == "back" : 
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue[0])
