import sys

def search(arr,start,end,C):
    result=1
    while start<=end:
         current=arr[0]
         count=1
         mid=(start+end)//2

         for i in range(1,len(arr)):
             if arr[i]>=mid+current:
                 count += 1
                 current=arr[i]
        
         if count>=C:
            result=mid
            start=mid+1
        
         else:
            end=mid-1

    return result
         
        

            
        
N,C=map(int,sys.stdin.readline().split())
x=[]
for i in range(N):
    x.append(int(sys.stdin.readline()))
x.sort()

start= 1
end=x[N-1]-x[0]

print(search(x,start,end,C))