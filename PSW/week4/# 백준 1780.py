
import sys 

N = int(sys.stdin.readline()) 
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def daq(x, y, size):
    
    global count_minus1, count_zero, count_one  # 전역변수 지정
    
    
    # 첫 번째 숫자를 기준으로 비교
    base = paper[x][y]
    sameNumber = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != base:  # 숫자가 다르면
                sameNumber = False
                break
        if not sameNumber:
            break

    if sameNumber:                   # 구역이 모두 동일한 숫자인 경우
        if base == -1:
            count_minus1 += 1
        elif base == 0:
            count_zero += 1
        else:
            count_one += 1
    else:                            # 구역이 다른 숫자로 이루어진 경우 9분할
        onethird_size = size // 3
        for i in range(3):           # 3x3 반복
            for j in range(3):
                daq(x + i * onethird_size, y + j * onethird_size, onethird_size)


# 결과 저장 변수
count_minus1 = 0
count_zero = 0
count_one = 0


# 분할 정복 실행
daq(0, 0, N)

# 출력
print(count_minus1)
print(count_zero)
print(count_one)
