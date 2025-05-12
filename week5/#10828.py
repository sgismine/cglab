import sys

n = int(sys.stdin.readline())

stack=[]                                       #스택초기화
for i in range(n):
    command = sys.stdin.readline().split()     #공백을 기준으로 나눔 push, 4같이

    if command[0]=='push':                     
        stack.append(command[1])               #스택에 맨뒤에 새로운 값 삽입
        
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())                 #맨위에 제거후 출력
            
    elif command[0] == 'size':
        print(len(stack))
        
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)                           #비었으면 1
        else:
            print(0)                           #안비어있으면 0
            
    elif command[0] == 'top':
        if len(stack)==0:                       
            print(-1)
        else:
            print(stack[-1])                   #맨위에 값 제거 안하고 출력
            
            
