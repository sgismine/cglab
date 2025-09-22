
n, k = map(int, input().split())  
items = [list(map(int, input().split())) for _ in range(n)] 

# dp[w] = 무게 w까지 넣을 수 있는 최대 가치
dp = [0] * (k + 1)


for w, v in items:
    for weight in range(k, w - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - w] + v) # 현재상태 넣는경우 vs 안넣는 경우


print(dp[k])
