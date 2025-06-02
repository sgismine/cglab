import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

arr=deque(range(1,n+1))
answer=[]

while(arr):
    for i in range(k-1):
        arr.append(arr.popleft())
    answer.append(arr.popleft())


print("<",end='')
for i in range(n-1):
    print(answer[i],end=', ')
print(answer[-1],end='')
print(">")