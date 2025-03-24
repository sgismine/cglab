n = input()  
arr = list(map(int,n)) 
num = len(arr)  

for i in range(num-1,0,-1):
    for j in range(0,i):
        if arr[j]<arr[j+1]:
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp

print("".join(map(str, arr)))  
