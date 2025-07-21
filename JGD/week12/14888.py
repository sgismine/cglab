# dfs로 가능한 모든 조합
# 최대값 최소값 저장
# 처음 풀이 -> 1번 테케만 맞고 나머지는 답 ㅈㄴ 이상하게 나옴;
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
num_ops = list(map(int, input().split()))

op_candidates = '+-*/'
ops = []
for i, op in enumerate(op_candidates):
    ops.extend([op] * num_ops[i])

result = []

for op in ops:
    val = nums[0]
    for i in range(N-1):
        if op == '+':
            val = (val+nums[i+1])
        elif op == '-':
            val = (val-nums[i+1])
        elif op == '*':
            val = (val*nums[i+1])
        else:
            val = int(val/nums[i+1])
    
        result.append(val)

print(max(result))
print(min(result))


# 2번째 풀이(지피티참고, 개똑똑하네 ㄹㅇ)

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

# 결과 저장용 변수
min_result = float('inf')
max_result = float('-inf')

# 백트래킹 함수
def dfs(index, current_result, add, sub, mul, div):
    global min_result, max_result

    # 모든 숫자를 다 사용했을 경우
    if index == n:
        min_result = min(min_result, current_result)
        max_result = max(max_result, current_result)
        return

    num = numbers[index]

    # 각각의 연산자에 대해 남아있으면 재귀 호출
    if add > 0:
        dfs(index + 1, current_result + num, add - 1, sub, mul, div)
    if sub > 0:
        dfs(index + 1, current_result - num, add, sub - 1, mul, div)
    if mul > 0:
        dfs(index + 1, current_result * num, add, sub, mul - 1, div)
    if div > 0:
        
        if current_result < 0:
            dfs(index + 1, -(-current_result // num), add, sub, mul, div - 1)
        else:
            dfs(index + 1, current_result // num, add, sub, mul, div - 1)

# 시작 숫자는 numbers[0]이고, 다음 숫자부터 index=1부터 시작
dfs(1, numbers[0], add, sub, mul, div)

# 결과 출력
print(max_result)
print(min_result)



