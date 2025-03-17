N = int(input())
ary = []


while(1) :
    k=N%10
    ary.append(k)
    N = int(N/10)
    if N == 0 :
        break

ary.sort()
ary.reverse()

for i in range(len(ary)) :
    print(ary[i],end='')
