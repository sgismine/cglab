# 1780 종이의 개수


def papercount(x ,y ,n):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j] :
                m = n // 3
                papercount(x, y, m)
                papercount(x + m, y, m)
                papercount(x + m + m, y , m)
                papercount(x, y + m, m)
                papercount(x, y + m + m, m)
                papercount(x + m, y + m, m)
                papercount(x + m + m, y + m, m)
                papercount(x + m, y + m + m, m)
                papercount(x + m + m, y + m + m, m)
                return
    if color == -1 :
        ans[0] += 1
    elif color == 0 :
        ans[1] += 1
    else :
        ans[2] += 1

    
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]
papercount(0,0,N)
for answer in ans :
    print(answer)

