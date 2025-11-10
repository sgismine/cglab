import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
q=list(range(1,n+1))
result=[]


num=0
for _ in range(n):
   num=(num+k-1)%len(q)
   out=q.pop(num)
   result.append(out)



print("<",end="")
for i in range(n-1):
   print(str(result[i])+",",end=" ")
print(str(result[n-1]),end="")
print(">")