import sys 

n=int(sys.stdin.readline())

lst=[]

for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    tmp.reverse() #reverse 해서 append
    lst.append(tmp)

lst.sort()

for i in lst:
    print(i[1],i[0])