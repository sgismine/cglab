import sys
n=int(sys.stdin.readline())

lst=[]

for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    lst.append(tmp) #lst는 이중리스트가 됨.

lst.sort()

for i in range(n):
    for j in range(2):
        print(lst[i][j],end=" ")
    print()