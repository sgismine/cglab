#처음에 그냥 sort썼는데 메모리 초과 -> 10000개의 리스트 만들고 인덱스 출력
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