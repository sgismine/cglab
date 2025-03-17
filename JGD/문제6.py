a=input()
lst=[]

for i in range(len(a)):
    tmp=int(a[i])
    lst.append(tmp)

lst.sort()
lst.reverse()

for i in range(len(lst)):
    print(lst[i],end="") #출력 형식 맞추기