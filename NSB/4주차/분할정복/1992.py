# 1992 쿼드트리

def QuadTree(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color :
                m = n // 2
                print("(", end = '')
                QuadTree(x, y, m)
                QuadTree(x , y + m, m)
                QuadTree(x + m, y, m)
                QuadTree(x + m, y+ m, m)
                print(")", end = '')
                return
    if color == 0 :
        print(0, end = '')
    else :
        print(1, end = '')


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

QuadTree(0, 0, N)

