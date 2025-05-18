# 2493 4번
# 스택 안써서 풀었는데 시간초과 걸려서 풀이 참고했습니다..

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
