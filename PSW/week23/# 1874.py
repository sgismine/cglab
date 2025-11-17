import sys

n = int(sys.stdin.readline())

stack = []          
operations = []     # +/- 저장
current_num = 1     # 1부터 n까지 오름차순으로 증가할 숫자
possible = True     # 수열 생성 가능 여부 

for _ in range(n):
    
    target = int(sys.stdin.readline()) 
    
    while current_num <= target:
        stack.append(current_num)
        operations.append('+')
        current_num += 1
        

    if stack[-1] == target:
        stack.pop()
        operations.append('-')
    else:
        # 스택의 top이 target보다 크다는 의미 (예: top=2, target=1)
        possible = False
        break

if possible:
    for op in operations:
        print(op)
else:
    print('NO')