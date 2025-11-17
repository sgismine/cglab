import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

answer = [-1] * N
stack = []

for i in range(N - 1, -1, -1):
    

    while len(stack) > 0 and stack[-1] <= A[i]:
        stack.pop(-1)

    stack.append(A[i])
    

    if len(stack) > 1 :
        answer[i] = stack[-2]
        
print(*answer)