import sys

n = int(sys.stdin.readline())
height = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
answer = 0

for h in height:
    
    while stack and stack[-1] <= h:
        stack.pop()
    
    answer += len(stack)
    stack.append(h)

print(answer)
