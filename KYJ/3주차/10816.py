import sys

N=int(sys.stdin.readline())
Narr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
Marr=list(map(int,sys.stdin.readline().split()))

Narr.sort()

dic={}
for i in Narr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for i in Marr:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')


"""
N=int(sys.stdin.readline())
Narr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
Marr=list(map(int,sys.stdin.readline().split()))

Narr.sort()
answer=[0]*M

for i in range(len(Marr)):
    start=0
    end=N-1
    count=0
    while start<=end:
        mid=(start+end)//2
        if Marr[i]<Narr[mid]:
            end=mid-1
        elif Marr[i]==Narr[mid]:
            count+=1
            l,r=mid-1,mid+1
            while l>=0 and Narr[l]==Marr[i]:
                count+=1
                l-=1
            while r<N and Narr[r]==Marr[i]:
                count += 1
                r+=1
            break
        else:
            start=mid+1
    answer[i]=count

for i in answer:
    print(i,end=" ")

#시간초과
"""
