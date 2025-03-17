N = int(input())
ary = []
for i in range(N) :
    k = list(map(int,input().split()))
    ary.append(k)


ary = sorted(ary, key=lambda x:x[1])

for i in range(N):
    for j in ary[i]:
        print(j,end=' ')
    print()
    

# 예제는 맞지만 오류남
