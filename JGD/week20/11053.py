import sys
input = sys.stdin.readline
 
N = int(input())
 
A = list(map(int, input().split()))
 
dp = [1] * N #가장 짧은 부분 수열의 길이가 1이기 때문에 1로 dp 테이블 초기화
 
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]: # A[i]와 A[0]~A[i-1]까지 값 하나씩 비교, 클때마다 해당 인덱스 dp테이블에는 1씩 더해줌
            dp[i] = max(dp[i], dp[j]+1)
 
print(max(dp))


# 참고 : 이진탐색으로 풀기
# dp는 O(n^2), 이진탐색은 O(nlogn)
# 이진 탐색은 모든 배열의 값을 일일히 비교하지 않음

# from bisect import bisect_left

# array = [5, 2, 1, 4, 3, 5]
# dp = [1]
# x = [array[0]]

# for i in range(1, len(array)):
#     if array[i] > x[-1]: # 현재 값이 x 배열의 마지막 값보다 클 경우
#         x.append(array[i]) # x 배열에 현재 값을 추가해 주고
#         dp.append(dp[-1] + 1) # 증가 부분 수열의 길이를 1 증가시킨다.
#     else: # 그렇지 않을 경우
#         idx = bisect_left(x, array[i]) # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
#         x[idx] = array[i] # x 배열의 idx 위치에 현재 값을 넣어준다.

# print(x)