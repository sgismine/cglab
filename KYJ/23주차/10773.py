import sys

k=int(sys.stdin.readline())
arr=[]

for _ in range(k):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        if len(arr)==0:
            continue
        arr.pop()
    else:
        arr.append(tmp)

result=0
for x in arr:
    result=result+x

print(result)
    
    
