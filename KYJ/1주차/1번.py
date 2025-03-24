n = int(input())
array =[]
for i in range(0,n,1):
    a=int(input())
    array.append(a)

for i in range (0,n-1,1):
    min = i
    for j in range(i+1,n,1):
        if (array[j] < array[min]):
            min = j

    temp = array[i]
    array[i]=array[min]
    array[min]=temp

for i in range(0,n,1):
    print(array[i])
            
    


    

    


