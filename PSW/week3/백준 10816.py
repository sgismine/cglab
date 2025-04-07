import sys
input = sys.stdin.readline
 
N = int(input())
N_list = sorted(map(int, input().split()))
M = int(input())
M_list = map(int, input().split())
 
#중복되는 값 +1씩 늘리고 처음 등장한 값 1로 저장해서 딕셔너리에 개수저장
dic = {}
for i in N_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
 
#이진탐색
def binarySearch(target, start, end):
    if start > end: #범위가 역전되면 -> 찾는 값이 없음 -> 0리턴
        return 0
    
    mid = (start + end) // 2 #가운데 인덱스 계산
    
    if target == N_list[mid]:
        return dic[target]  #찾았으면 -> dic에서 해당 숫자의 개수 리턴
    
    elif target > N_list[mid]:
        return binarySearch(target, mid + 1, end) #찾는 값이 mid보다 크면 -> 오른쪽반(mid+1)으로 재귀탐색
    
    elif target < N_list[mid]:
        return binarySearch(target, start, mid - 1) #찾는 값이 mid보다 작으면 -> 왼쪽반(mid-1)으로 재귀탐색
 
for target in M_list:
    print(binarySearch(target, 0, N - 1), end=" ")

#card_list에 있는 숫자들을 하나씩 binarySearch로 탐색
#각 숫자가 my_list에 몇 개 있는지 출력.
#없으면 0
#있으면 dic에서 찾아서 출력

#end=" ": 한 줄에 공백으로 구분해서 출력.