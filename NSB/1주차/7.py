N = int(input())
ary = []
for i in range(N) :
    k = list(map(int,input().split()))
    ary.append(k)


ary.sort()

for i in range(N):
    for j in ary[i]:
        print(j,end=' ')
    print()
    