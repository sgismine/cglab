n,k=map(int,input().split())

arr=list(map(int,input().split()))[:n]

for i in range(n-1,0,-1):
    for j in range(0,i):
        if arr[j]<arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp


print(arr[k-1])


