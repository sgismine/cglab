#시간 줄이기 위해서 sys 사용
import sys

n=int(sys.stdin.readline())
lst=[]

for i in range(n):
    tmp=int(sys.stdin.readline())
    lst.append(tmp)

lst.sort()

for i in range(n):
    print(lst[i])