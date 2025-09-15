import sys
input = sys.stdin.readline

n = int(input())

dp = [] 
dp.append(0) #f0 = 0
dp.append(1) #f1 = 1

for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2]) # f(n) = f(n-1)+f(n-2)

print(dp[n])