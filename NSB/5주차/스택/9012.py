# 9012 2번
import sys

N = int(input())

for i in range(N):
    pares = list(sys.stdin.readline().rstrip())
    VPS = "True"
    stack = []
    for pare in pares :
        if pare == '(' :
            stack.append(pare)
        elif pare == ')' :
            if len(stack) == 0 :
                VPS = "False"
            else :
                stack.pop()
    if len(stack) == 0 and VPS == "True":
        ans = "YES"
    else :
        ans = "NO"
    print(ans)
    
