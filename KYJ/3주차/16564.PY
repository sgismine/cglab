import sys

def search(arr,K,start,end):
    result=0
    while start<=end:
        count=0
        mid=(start+end)//2

        for i in range(len(arr)):
            if arr[i]<mid:
                count += mid-arr[i]

        if count<=K:
            result=mid
            start=mid+1
    
        else:
            end=mid-1

    return result


N,K=map(int,sys.stdin.readline().split())
X=[]
for i in range(N):
    X.append(int(sys.stdin.readline()))
X.sort()
start=X[0]
end=X[N-1]+K #처음에 k를 안 더해주니까 정답처리 안됨 -> 제일 큰값보다 높은값이 정답이 될수있는데 K를 더하지 않으먼 높은값을 조사할 수 없기 때문
print(search(X,K,start,end))
