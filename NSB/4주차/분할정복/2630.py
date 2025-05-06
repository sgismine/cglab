# 2630 색종이 만들기

def cut(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color :
                m = n // 2
                cut(x, y, m)
                cut(x, y+m, m)
                cut(x+m, y, m)
                cut(x+m, y+m, m)
                return
    if color == 0 :
        ans[0] += 1
    else :
        ans[1] += 1
                

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]
cut(0, 0, N)

for answer in ans:
    print(answer)




