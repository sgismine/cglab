# 5639 이진검색트리

import sys

sys.setrecursionlimit(10 ** 9)  # 재귀호출 깊이 제한 변경
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break


def pretopost(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    pretopost(start + 1, mid - 1)  # 왼쪽
    pretopost(mid, end)  # 오른쪽
    print(pre[start])  # 루트


pretopost(0, len(pre) - 1)