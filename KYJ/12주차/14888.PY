import sys


N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split())) 

maximum=int(-1e9)
minimum=int(1e9)

def dfs(depth,total,plus,minus,mult,div):
    global maximum,minimum
    if depth==N:
        maximum=max(maximum,total)
        minimum=min(minimum,total)
        return
    
    if plus>0:
        dfs(depth+1,total+number[depth],plus-1,minus,mult,div)
    if minus>0:
         dfs(depth+1,total-number[depth],plus,minus-1,mult,div)
    if mult>0:
         dfs(depth+1,total*number[depth],plus,minus,mult-1,div)
    if div>0:
         dfs(depth+1,total//number[depth],plus,minus,mult,div-1)


dfs(1,number[0],op[0],op[1],op[2],op[3])
print(maximum)
print(minimum)
