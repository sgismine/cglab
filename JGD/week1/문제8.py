import sys 

n=int(sys.stdin.readline())

lst=[]

for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    tmp.reverse()
    lst.append(tmp)

lst.sort()

for i in lst:
    print(i[1],i[0])
    