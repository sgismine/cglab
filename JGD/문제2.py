lst=[]
# a=int(input())
# lst.append(a)
# b=int(input())
# lst.append(b)
# c=int(input())
# lst.append(c)
# d=int(input())
# lst.append(d)
# e=int(input())
# lst.append(e)
for i in range(5):
    tmp = int(input())
    lst.append(tmp)

lst.sort()
print(sum(lst)//len(lst))
print(lst[2])


