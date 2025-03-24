import sys

N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(sys.stdin.readline())

array=list(set(arr))

#array=[]
#for i in range(N):
    #if arr[i] not in array:
        #array.append(arr[i]) #이렇게도 가능한데 메모리 더 많이 소요요


array.sort(key = lambda x:(len(x),x))


for i in array:
    print(i,end='')

