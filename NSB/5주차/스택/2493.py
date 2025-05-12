# 2493 4번

import sys
N = int(input())
top = list(map(int,sys.stdin.readline().split()))

stack = []
ans = [0] * N


for i in range(N):
    while stack :
        if stack[-1][1] >= top[i] :
            ans[i] = stack[-1][0] + 1
            break
        else :
            stack.pop()

    stack.append((i, top[i]))

print(*ans)
