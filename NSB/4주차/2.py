# 2110

import sys
N, C = map(int,sys.stdin.readline().split()) # N = 집의 개수 C = 공유기의 개수
arr = []
for i in range(N) :
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]
ans = 0

while start <= end :
    mid = (start + end) // 2
    current = arr[0]
    count = 1

    for i in range(1,len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
        
    if count >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)

