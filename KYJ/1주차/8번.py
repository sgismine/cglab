n=int(input())
points=[]

for i in range(0,n):
    x, y = map(int, input().split())
    points.append((x, y))



#for i in range(n-1,0,-1):
    #for j in range(0,i):
        #if(points[j][1]>points[j+1][1]) or (points[j][1]==points[j+1][1] and points[j][0]>points[j+1][0]):
            #tmp=points[j+1]
            #points[j+1]=points[j]
            #points[j]=tmp

points.sort(key=lambda p: (p[1], p[0]))

for x,y in points:
    print(x,y)


