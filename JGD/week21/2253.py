# 2차원 dp
# 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n,m = map(int,input().split())
MAX = 10001 #n이 2~10000
dp = [[-1]*150 for i in range(MAX)] #dp의 초기값 -1로, 경우의 수 없으면 -1 출력이니까
# 점프길이는 10000의 제곱근 정도인 150으로 제한 (계속 1씩 증가했을 때 점프 길이의 최대치가 150이됨)

ch = [0 for i in range(n+1)] 
flag = False

for i in range(m):
    idx = int(input()) # 작은돌 입력 받은 곳은 1로
    ch[idx] = 1

def solution(idx,jump):
    global flag
    if idx == n: #현재 돌 위치가 최종 돌 위치에 도달하면
        flag = True
        return 0
    
    if dp[idx][jump] != -1: #이전에 방문했었다면, dp테이블 정보 재활용
        return dp[idx][jump]
    
    dp[idx][jump] = sys.maxsize #비교하기 쉽게 매우큰 수 넣어두기
    for i in range(-1,2): # jump에서 -1,0,1 칸 이동하므로
        if jump+1 >=1: #이동 가능 조건
            next = idx+(jump+i) # 현재 위치에서 점프+i만큼 이동한 위치
            if next <= n and ch[next] != 1: #범위내, 작은돌 아니면
                dp[idx][jump] = min(dp[idx][jump],1+solution(next,jump+i))
                #지금위치에서 점프한거랑 한번 뛰고 그 이후 경로에서 최소 점프 횟수 중 최솟값

    
    return dp[idx][jump]


res = solution(1,0)

if flag:
    print(res)
else:
    print(-1)