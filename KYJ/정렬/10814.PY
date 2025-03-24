import sys

N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    age,name=sys.stdin.readline().split()
    arr.append((int(age),name))


arr.sort(key=lambda x:x[0])

for x,y in arr:
    print(x,y)

