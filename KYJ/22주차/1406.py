import sys


s = sys.stdin.readline().strip()
m=int(sys.stdin.readline())
left=[]
right=[]
result=[]

for x in s:
    left.append(x)


for _ in range(m):
    arr=list(map(str,sys.stdin.readline().strip().split()))

    if arr[0]=='L':
        if len(left) != 0:
            right.append(left.pop())
    
    if arr[0]=='D':
        if len(right) != 0:
            left.append(right.pop())
    
    if arr[0]=='B':
        if len(left) != 0:
            left.pop()
    
    if arr[0]=='P':
        left.append(arr[1])

result.append(''.join(left + right[::-1]))

for x in result:
    print(x)



