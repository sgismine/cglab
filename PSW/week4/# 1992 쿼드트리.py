# 백준 1992 쿼드트리 

import sys


def daq(x, y, size):                            # x = rol, y = col
    if size == 1:                               # 구역이 1x1인 경우
        print(arr[x][y], end="")
        return
    
    
    base = arr[x][y]                            # 첫번째 칸 숫자
    sameColor = True                            # 구역 내 숫자가 같을 때 = True
    
    # 현재 구역이 동일한 숫자로 이루어졌는지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != base:
                sameColor = False               # 구역 내 숫자가 다를때
                break                           # 내부 루프 종료
        if not sameColor:                       # 외부 루프 종료
            break
    
    
    if sameColor:                               # 구역이 동일한 숫자로 이루어진 경우
        print(sameColor, end="")
    else:                                       # 구역이 다른 숫자로 이루어진 경우
        print("(", end="")
        half = size // 2
        daq(x, y, half)                         # 1사분면
        daq(x, y + half, half)                  # 2사분면
        daq(x + half, y, half)                  # 3사분면
        daq(x + half, y + half, half)           # 4사분면
        print(")", end="")                      # 닫는 괄호


# 입력 처리
n = int(input())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 분할 정복 실행
daq(0, 0, n)
