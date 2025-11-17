import sys

N = int(sys.stdin.readline())

Stack = []


for _ in range(N):
    num = int(sys.stdin.readline()) 
    
    if Stack and num == 0: 
        Stack.pop()
    else:
        Stack.append(num)
        
print(sum(Stack))