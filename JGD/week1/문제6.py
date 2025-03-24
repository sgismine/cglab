a=input()
lst=[]

for i in range(len(a)):
    tmp=int(a[i])
    lst.append(tmp)

lst.sort()
lst.reverse()

for i in range(len(lst)):
    print(lst[i],end="")