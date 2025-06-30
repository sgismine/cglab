# 딕셔너리
tree = {}


n = int(input())

# 트리 입력 받기
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right) #왼쪽 자식 오른쪽 자식을 입력받아 tree 딕셔너리에 저장
                               #빈거는 '.'으로 저장

# 전위 순회 (루트 → 왼쪽 → 오른쪽)
def preorder(node):
    
    # 자식 없는 경우
    if node == '.': 
        return '' # 종료
    left, right = tree[node]   #현재 노드의 왼쪽 자식과 오른쪽 자식을 가져오는 역할
    return node + preorder(left) + preorder(right) #여기서 가져온 노드 사용

# 중위 순회 (왼쪽 → 루트 → 오른쪽)
def inorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return inorder(left) + node + inorder(right)

# 후위 순회 (왼쪽 → 오른쪽 → 루트)
def postorder(node):
    if node == '.':
        return ''
    left, right = tree[node]
    return postorder(left) + postorder(right) + node

# 루트는 항상 'A'로 고정
print(preorder('A')) #전위
print(inorder('A'))  #중위
print(postorder('A')) #후위
