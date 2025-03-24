# 답은 나오눈데 시간 초과 해결 못했음 ㅜ
# start랑 end값을 cut이랑 end를 비교하면서 줄여나감
# cut이 m보다 크거나 같다 -> 아직 비교할 수 있는 경우의 수가 존재 -> start를 mid+1로 수정해서 다시 이분 탐색
# cut이 m보다 작다 -> 경우의 수 x -> end를 줄임
# 줄여가다 보면 결국 end 값이 정답이 됨

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
