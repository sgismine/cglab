import sys
from collections import deque
n=int(sys.stdin.readline())
arr=deque(range(1,n+1))

while(len(arr)>1):
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])




#n=int(sys.stdin.readline())
#arr=list(range(1,n+1))
#while(len(arr)>1):
    #arr.pop(0)
    #tmp=arr.pop(0)
    #arr.append(tmp)

#print(arr[0])
#시간 초과 코드