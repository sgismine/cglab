import sys

N=int(sys.stdin.readline())
P=[]
for i in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    P.append(a)

answer=[]

def function(x,y,n):
    color=P[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color !=P[i][j]:
                for a in range(2):
                    for b in range(2):
                        function(x+(n//2)*a,y+(n//2)*b,n//2)
                return
    if color == 0 :
        answer.append(0)
    else:
        answer.append(1)

function(0,0,N)
print(answer.count(0),answer.count(1),sep='\n')
