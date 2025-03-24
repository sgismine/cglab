arr=[None]*5
sum=0

for i in range(0,5):
    tmp=int(input(" "))
    sum=sum+tmp
    arr[i]=tmp
avr=int(sum/5)

for i in range(4,0,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            temp=arr[j]+1
            arr[j+1]=arr[j]
            arr[j]=temp

center=arr[2]

print(avr)
print(center)



