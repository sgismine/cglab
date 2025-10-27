import sys

n,m=map(int,sys.stdin.readline().split())
stone=[0]*m
dp= [[10001]* (int((2*n)**0.5)+2)  for _ in range(n+1)]

for i in range(m):
    stone[i]=sys.stdin.readline()

dp[1][0] =0
for i in range(2,n+1):
    if i in stone:
        continue
    for x in range(1,int((2*i)**0.5)+1):
        dp[i][x]=min(dp[i-x][x-1],dp[i-x][x],dp[i-x][x+1])+1

ans=min(dp[n])

if ans==10001:
    print(-1)
else:
    print(ans)








'''
int((2*N)^0.5)의 의미
-> 불필요한 연산을 막기 위한 연산
등차수열의 합 공식 = k(2a+(k-1)d) / 2
(이 문제에서 a(첫 번째 수) =1, d(공차) =1 )
따라서 마지막에 있는 돌까지 가장 빠르게 갈 수 있는 돌들의 수의 합 N
= k(k+1)/2
k = (2N-k)^0.5 <= 2N^0.5
'''