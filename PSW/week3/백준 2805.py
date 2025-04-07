# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split()) 
# #N: 나무의 수
# #M: 필요한 나무 길이의 총합



# trees = list(map(int, input().split())) 

# low, high = 0, max(trees)
# #left: 자를 수 있는 최소 높이 (0)
# #right: 자를 수 있는 최대 높이 (가장 높은 나무)



# while low <= high: #탐색범위 지정
#     mid = (low + high) // 2 #중간값을 자르는 높이로 설정 → 이 높이로 잘랐을 때 얻을 수 있는 나무 총합을 계산


#     total = 0 #나무길이 총합 초기화

#     for tree in trees:
#         if tree >= mid:
#             total += tree - mid
            
#             #각 나무를 mid 높이로 자를 경우 잘려나오는 나무의 길이 누적
#             #나무가 20이고 mid=15면 20 - 15 = 5만큼 나옴
#             # #tree < mid면 잘리지 않음


            

#     if total >= M:
#         low = mid + 1
        
#         #잘라낸 나무의 총합이 M보다 크거나 같으면 → 더 높게 자를 수 있음 → low(-> mid+1)를 올림


#     else:
#         high = mid - 1
#         #잘라낸 나무의 총합이 M보다 작으면 → 더 낮게 잘라야함 → high(-> mid-1)를 올림

# print(high)
# #이분 탐색이 끝난 후 high는 조건을 만족하는 가장 높은 높이를 의미함


#1년전 풀이
N, M = map(int, input().split())

trees = list(map(int, input().split()))

L = 0
R = max(trees)

while L <= R:
    mid = (L + R) // 2
    result = 0
    
    for tree in trees:
        if tree >= mid:
            result += tree - mid
            
    if result >= M:
        L = mid + 1 
    else:
        R = mid - 1
        
print(R)