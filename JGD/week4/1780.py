import sys

n = int(sys.stdin.readline())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for i in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    papers.append(row)

def check(row,col,n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = papers[row][col] # 현재 종이 색

    for i in range(row, row + n):
        for j in range(col,col + n):
            if papers[i][j] != curr:
                next_n = n//3 # 다음 종이의 길이는 1/3

                check(row,col,next_n) #왼쪽 위
                check(row,col+next_n,next_n) # 위쪽 가운데
                check(row,col+(2*next_n),next_n) # 오른쪽 위
                check(row + next_n, col, next_n) # 가운데 왼쪽
                check(row + next_n, col + next_n, next_n)   # 정가운데
                check(row + next_n, col + (2 * next_n), next_n)  # 가운데 오른쪽
                check(row + (2 * next_n), col, next_n)  # 아래 왼쪽
                check(row + (2 * next_n), col + next_n, next_n)  # 아래 가운데
                check(row + (2 * next_n), col + (2 * next_n), next_n) # 아래 오른쪽 
                return
            
    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return


check(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)