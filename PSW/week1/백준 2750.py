N = int(input())

list =[]

for i in range(N) :
    list.append(int(input()))
    
list.sort()

for i in list :
    print(i)
    

#print(list)로 출력하면 [1, 2, 3, 4, 5] 일케 출력됨
