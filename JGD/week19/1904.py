# n= 1 -> 1
# n=2 -> 2
# n=3 -> 3
# n=4 -> 5 ( 0011, 0000, 1001, 1100, 1111 )
# n=5 -> 8 ( 11111,11100,11001,10011,00111, 00001,00100,10000, )
# f(n) = f(n-1) + f(n-2)


# 메모리초과 -> dp 테이블 크기를 제한 안해서 그런가?
# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = []
# dp.append(0) #f(0) = 0
# dp.append(1) #f(1) = 1
# dp.append(2) #f(2) = 2

# for i in range(3,n+1):
#     dp.append(dp[i-1]+dp[i-2])

# print(dp[n]%15746)


import sys
input = sys.stdin.readline

n = int(input())

dp =[0]*n
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n]%15746)