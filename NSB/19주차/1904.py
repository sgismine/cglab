# 1904 01타일
import sys
input = sys.stdin.readline

n = int(input())
tile = [0]*(n+1)

tile[1] = 1
tile[2] = 2

for i in range(3,n+1):
    tile[i] = (tile[i-1] + tile[i-2])%15746

print(tile[n])

