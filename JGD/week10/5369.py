# 전위순회 결과를 트리로 만듬(루트보다 작으면 왼쪽 서브트리,크면 오른쪽 서브트리)
# 후위순회(왼-오-루)

import sys
input = sys.stdin.readline

lst = [] #전위순회 결과를 리스트로

while True:
    try:
        lst.append(int(input()))
    except:
        break

def postorder(start,end):
    if start>end:
        return
    root = lst[start] #0이 들어갈거니까. 전위순회는 무조건 처음이 루트임
    split = start+1 # 왼쪽 서브트리와 오른쪽 서브트리를 구분할 경계포인트 

    while split <=end and lst[split] < root : #루트보다 커지는 부분부터 오른쪽 서브트리
        spilt += 1

    postorder(start+1,split-1) #왼쪽 서브트리
    postorder(split,end)
    print(root)


postorder(0,len(lst)-1)

    
