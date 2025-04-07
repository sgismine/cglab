# 최장 증가 부분 수열 (LIS)를 알아야한다고 합니다.
# DP를 이용한 LIS : O(n^2)
# 이분 탐색을 활용한 LIS : O(NlogN)
# 아마 문제에 비해서 시간 제한이 빡세서 골드2인듯.

import sys
from bisect import bisect_right

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lis = [lst[0]]

for i in range(1,n): # 0번 인덱스는 이미 저장해뒀으므로 0~n이 아니고, 1~n
    target = lst[i]
    if lis[-1] < target: # target이 LIS의 제일 마지막 값과 비교해서 target이 더 크다면 LIS에 추가
        lis.append(target)
    else: # target이 더 작다면 이분 탐색을 통해 lis 값 중 target보다 크면서 제일 작은 값으로 target 초기화
        idx = bisect_right(lis,target)
        print("idx : ",idx)
        lis[idx] = target

print(lis)
print(len(lis))

