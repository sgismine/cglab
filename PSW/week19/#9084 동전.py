import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M + 1)
    dp[0] = 1  # 0원을 만드는 방법 1가지
    
    for coin in coins:
        for amount in range(coin, M + 1):
            dp[amount] += dp[amount - coin]
    
    print(dp[M])
