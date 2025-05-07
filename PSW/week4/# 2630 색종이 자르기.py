# 백준 2630 색종이 자르기

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def daq(x, y, N):
    color = paper[x][y]                 # 첫 번째 색상
    sameColor = True                    # 구역 내 색상이 같을 때 = True
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j] != color:
                sameColor = False       # 구역 내 색상이 다를 때
                break                   # 내부 루프 종료
            if not sameColor:           # 외부 루프 종료
                break
            
            
    if sameColor: 
        # 구역 내 색상이 동일 한 경우
        # 흰색 블록 반환 (1,0), 파란색 블록 반환(0,1)
        return (1,0) if color == 0 else(0,1)
    
    # 색상이 다르면 4분할하여 재귀 호출
    else: 
        half = N // 2
        q1 = daq(x, y, half)                   # 1사분면(1쿼터)
        q2 = daq(x, y + half, half)            # 2사분면(2쿼터)
        q3 = daq(x + half, y, half)            # 3사분면(3쿼터)
        q4 = daq(x + half, y + half, half)     # 4사분면(4쿼터)
        
        # 결과계산
        return (q1[0] + q2[0] + q3[0] + q4[0],  # 흰색(0) 개수 합산
                q1[1] + q2[1] + q3[1] + q4[1])  # 파란색(1) 개수 합산 
        

white, blue = daq(0, 0, N)
print(white)
print(blue)

        
        
        