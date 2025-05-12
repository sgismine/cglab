lst = list(input())
stack = []
num = 1 # 계산을 위한 값
result = 0

for i in range(len(lst)):
    if lst[i] == "(" :
        num *= 2
        stack.append(lst[i])
    elif lst[i] == "[" :
        num *= 3
        stack.append(lst[i])
    elif lst[i] == ")" :
        if not stack or stack[-1] != "(" :
            result = 0
            break
        if lst[i-1] == "(" :
            result += num
        num //=2
        stack.pop()

    elif lst[i] == "]":
        if not stack or stack[-1] != '[':
            result = 0
            break
        if lst[i-1] == '[':
            result += num
        num //= 3
        stack.pop()


if stack : 
    print(0)
else:
    print(result)