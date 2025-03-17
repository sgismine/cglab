ary = []
sum = 0
for i in range(5) :
    ary.append(int(input()))
    sum = sum + ary[i]

ary.sort()

print(int(sum/5))
print(ary[2])
