import sys


## 아 줴줴이야
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))



stack=[]
result=[]
for i in arr:
    while stack and stack[-1] <= arr[i]:
        tmp=stack.pop()
        for x in range(i):
            result[x]=tmp

    stack.append(arr[i])
    

print(result)
