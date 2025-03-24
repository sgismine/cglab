lst=[]

for i in range(5):
    tmp = int(input())
    lst.append(tmp)

lst.sort()
print(sum(lst)//len(lst))
print(lst[2])