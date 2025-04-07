# 16564

import sys
N, K = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(input()))

start = min(arr)
end = max(arr)

while start <= end :
    mid = (start + end) // 2
    sum = 0
    for i in arr:
        if mid > i:
            sum += mid - i
    if sum > K:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)

# 왜 틀렸노..