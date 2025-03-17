n=int(input())
lst=[]

for i in range(n):
    a=int(input())
    lst.append(a)

lst.sort()

for i in range(n):
    print(lst[i])
