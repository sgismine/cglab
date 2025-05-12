# 2504 3번
# 일단 이해하긴 했는데 다시 풀면 풀 자신 없음..

import sys

pare = list(sys.stdin.readline().rstrip())

stack = []
value = 1
ans = 0
for i in range(len(pare)) :
    if pare[i] == '(' :
        stack.append(pare[i])
        value *= 2

    elif pare[i] == ')' :
        if not stack or stack[-1] == '[' :
            ans = 0
            break
        if pare[i-1] == '(' :
            ans += value

        stack.pop()
        value //= 2

    elif pare[i] == '[' :
        stack.append(pare[i])
        value *= 3

    elif pare[i] == ']' :
        if not stack or stack[-1] =='(' :
            ans = 0
            break
        if pare[i-1] == '[' :
            ans += value
   
        stack.pop()
        value //= 3

if stack:
    print(0)

else :
    print(ans)
