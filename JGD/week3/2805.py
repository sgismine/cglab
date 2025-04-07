import sys

n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(lst)

while start <= end:

    mid = (start + end) // 2
    cut = 0

    for i in range(n):
        if lst[i] <= mid:
            cut += 0 
        else :
            cut += lst[i] - mid
    
    if cut >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
