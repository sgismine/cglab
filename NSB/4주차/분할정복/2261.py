# 2261 가장 가까운 두 점

N = int(input())
dot = []
for i in range(N) :
    x, y = map(int,input().split())
    dot.append([x,y])

dot.sort()

def distance_squared(x1,y1,x2,y2) :
    result = pow(abs(x1-x2)) + pow(abs(y1-y2))
    return result
