T = int(input())

for i in range(T):
    stack = []               #스택초기화
    
    x = input()              #입력된 괄호 문자열 x를 하나씩처리
    for j in x:
        if j == '(':
            stack.append(j)  #j를 스택에 추가
            
        elif j == ')':       #닫는괄호 기준
            if stack:
                stack.pop()  #스택이 안비어있으면 pop으로 짝을 맞춘 후 괄호를 제거
            else: 
                print("NO")  #스택이 비어있응경우 -> 짝이 안맞는 경우
                break
    else:
        if not stack: 
            print("YES")     #괄호문자열 모두 처리 -> 스택비어있음 -> 짝을 맞춤
        else: 
            print("NO")      #여는 괄호가 짝을 찾지 못함