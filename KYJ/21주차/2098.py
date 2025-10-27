import sys

n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dp=[[-1]*(1<<n)for _ in range(n)]


def dfs(row,visit,start,cnt):
    if cnt==n:
        return 0
    
    if dp[row][visit]!=-1:
        return dp[row][visit]
    
    ret=10000000
    for i in range(n):
        if visit & (1<<i) != 0 or graph[row][i]==0:
            continue
        if (cnt == n -1 and i != start) or (cnt != n-1 and i == start):
            continue

        ret = min(ret,dfs(i,visit | (1<<i),start,cnt+1)+graph[row][i])

    dp[row][visit]=ret

    return dp[row][visit]
    

print(dfs(0,0,0,0))