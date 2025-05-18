# # 3190 3번
# 뭔 소린지 하나도 모르겠습니다. 죄송합니다.

# 내가 푼거(입력받고 배열만 만듦..)
# import sys
# N = int(sys.stdin.readline())
# arr = [[0] * N for _ in range(N)]
# time = [0] * (N*N)

# K = int(sys.stdin.readline())
# for i in range(K) :
#     row, col = map(int,sys.stdin.readline().split())
#     arr[row-1][col-1] = 2


# L = int(sys.stdin.readline())
# for i in range(L):
#     X, C = map(str,sys.stdin.readline().split())
#     X = int(X)
#     time[X] = C

# for i in range(N):
#     for j in range(N):
#         print(arr[i][j],end=' ')
#     print()
# print(time)

# 일단 답지
from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break

print(cnt)
