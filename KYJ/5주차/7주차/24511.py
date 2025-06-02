import sys
from collections import deque

N=int(sys.stdin.readline())
structure_list=list(map(int,sys.stdin.readline().split())) 
atomic_list=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

queue=deque()
for i in range(N):
    if structure_list[i]==0:
        queue.append(atomic_list[i])

for i in range(M):
    item=arr[i]
    queue.appendleft(item)
    print(queue.pop(),end=' ')
    

#시간초과
'''import sys
from collections import deque

N=int(sys.stdin.readline())
structure_list=list(map(int,sys.stdin.readline().split())) 
atomic_list=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))


queuestack=[]
for i in range(N):
    if structure_list[i]==0:
        queuestack.append(deque([atomic_list[i]]))
    else:
        queuestack.append(deque([atomic_list[i]]))

for i in range(M):
    item=arr[i]
    for j in range(N):
        if structure_list[j]==0:
            queuestack[j].append(item)
            item=queuestack[j].popleft()
    else:
        queuestack[j].append(item)
        item=queuestack[j].pop()
    print(item,end=' ')'''

        


