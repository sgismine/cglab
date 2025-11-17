import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stack = []

# 내가 볼 수 있는이 아닌, 나를 볼 수 있는 빌딩 기준으로 생각하기
for i in range(n):
    top = int(input())
    while stack and stack[-1] <= top : # 자신 왼쪽에 자기보다 높은 빌딩이 있으면 확인불가
        stack.pop() # 확인할 수 없으므로 삭제시킴
    cnt += len(stack) # 스택엔 자기를 확인할 수 있는 친구들만
    stack.append(top) #다음 빌딩이 확인 할 수 있게 자신을 push

print(cnt)