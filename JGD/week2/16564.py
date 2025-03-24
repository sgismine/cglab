# mid값에서 각 캐릭터의 레벨을 빼서 올릴 수 있는 level을 설정
# level과 k를 비교
# level이 k보다 작거나 같으면 level을 더 올릴 수 있는 경우의 수 존재 -> start 수정
# level이 k보다 크면 level을 더 올릴 수 있는 경우의 수 x -> end를 수정하면서 mid의 최대값 찾기
# 결국 반복문이 끝났을 때 mid값이 목표값이 됨

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
