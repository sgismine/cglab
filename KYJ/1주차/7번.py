n = int(input())
points = []*n  

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))  

##for i in range(n-1,0,-1):
    #for j in range(0,i):
        #if points[j]>points[j+1]:
            #tmp=points[j+1]
            #points[j+1]=points[j]
            #points[j]=tmp

points.sort()

for x, y in points:
    print(x, y)  

