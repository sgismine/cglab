import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arrw = [0] * (n + 1)
arrv = [0] * (n + 1)

for i in range(1, n + 1):
    w, v = map(int, input().split())
    arrw[i] = w
    arrv[i] = v


dp = [0] * (k + 1)

for i in range(1, n + 1):
    w, v = arrw[i], arrv[i]
    if w > k:
        continue
    
    for j in range(k, w - 1, -1):
        
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[k])


        

