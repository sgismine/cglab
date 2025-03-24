import sys

def get_wood(tree,height):
    total=0

    for i in tree: 
        if i>height:
            total += i-height
    return total

def find_max_wood(tree,M,start,end):
    
    result=0

    while start<=end:
        mid=(start+end)//2
        wood=get_wood(tree,mid)

        if wood>= M:
            result = mid
            start=mid+1
        else:
            end=mid-1
    return result


N,M=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))
start=0
end=max(tree)
answer=find_max_wood(tree,M,start,end)
print(answer)