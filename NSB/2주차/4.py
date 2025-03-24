# 2805

import sys
N, M = map(int,sys.stdin.readline().split()) # N = 나무의 수 M = 필요한 나무 길이
tree = list(map(int,sys.stdin.readline().split()))  # tree = 각 나무의 길이
start = 0
end = max(tree) - 1
ans = 0
while start <= end :
    mid = (start + end) // 2
    sum = 0
    for i in range(N) :
        if mid < tree[i] :
            sum = sum + tree[i] - mid
    if sum == M :
        ans = mid
        break
    elif sum < M :
        end = mid -1
    else :
        start = mid + 1
    ans = mid - 1
print(ans)

