import sys

n,k = map(int,sys.stdin.readline().split())
lst = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    lst.append(tmp)

start = min(lst)
end = max(lst)

while start <= end:
    mid = (start + end) // 2
    level = 0
    for i in lst:
        if mid - i >= 0:
            diff = mid - i
            level += diff

    if level <= k:
        result = mid
        start = mid+1
    else:
        end = mid -1

print(result)