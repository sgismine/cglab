import sys

n = int(sys.stdin.readline())
papers = []

for _ in range(n):
    row = list(map(int,sys.stdin.readline().rsplit()))
    papers.append(row)

blue_cnt, white_cnt = 0, 0

def check(row,col,n):
    global blue_cnt, white_cnt

    curr = papers[row][col] #현재 칸 색상
    for i in range(row, row + n):
        for j in range(col, col + n):
            if curr != papers[i][j]:
                next_n = n // 2 # 길이 절반으로
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                return
    if curr == 0:
        white_cnt += 1
    else:
        blue_cnt += 1
    return

check(0,0,n)
print(white_cnt)
print(blue_cnt)