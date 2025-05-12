#9012 괄호
n=int(input())
for i in range(n):
    a=input()
    lst=[]
    for j in a:
        if j=="(":
            lst.append(j)
        else:
            if len(lst)==0:
                lst.append(j)
                break
            else:
                lst.pop()
    if len(lst)==0:
        print("YES")
    else:
        print("NO")
