import sys

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

a=sorted(set(arr))
answer=[]

for i in range(N):
    for j in range(len(a)):
        if a[j]==arr[i]:
            answer.append(j)


for i in answer:
    print(i,end=" ")

#시간 초과