# 4번과 5번은 메모리 제한이 다름. -> 4번을 실행했을 때 메모리는
# 76MB 이므로 파이썬의 sort를 쓰면 메모리 제한이 걸림 
# 4번과 5번의 차이는 수의 범위 차이 : 1,000,000 vs 10,000
# 10000개의 리스트 먼저 정의해놓고 인덱스 값 출력.

import sys

n=int(sys.stdin.readline())
lst=[0]*10000

for i in range(n):
    a=int(sys.stdin.readline())
    lst[a-1]+=1

for i in range(10000):
    if lst[i]!=0:
        for j in range(lst[i]):
            print(i+1)