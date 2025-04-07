# 2805

import sys
N, M = map(int,sys.stdin.readline().split()) # N = 나무의 수 M = 필요한 나무 길이
tree = list(map(int,sys.stdin.readline().split()))  # tree = 각 나무의 길이
start = 0
end = max(tree)
ans = 0
while start <= end :
    mid = (start + end) // 2
    sum = 0
    for i in tree :
        if mid < i :
            sum = sum + i - mid
    if sum < M :
        end = mid -1
    else :
        ans = mid
        start = mid + 1
print(ans)

# 시간 초과

