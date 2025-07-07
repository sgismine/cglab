import sys
sys.setrecursionlimit(10**5)  # 노드가 최대 10,000개니까


preorder = []
for line in sys.stdin: # 입력 기수를 모를때 표쥰입력으로 한 줄씩 읽어오기
    if line.strip():   # 공백제거 
        preorder.append(int(line.strip())) # 공백제거로 int 변환 가능


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# 현재 노드 값보다 작으면 왼쪽 크면 오른쪽으로 삽입
# 왼쪽 노드 < 부모노드 < 오른쪽 노드
def insert(root, key):
    if key < root.key:
        if root.left is None:
            root.left = Node(key)
        else:
            insert(root.left, key) 
    else:
        if root.right is None:
            root.right = Node(key)
        else:
            insert(root.right, key)

root = Node(preorder[0])  # 항상 첫 값을 루트노드로 설정
for key in preorder[1:]:   # 나머지는 순서대로 ~~~ insert gkatn
    insert(root, key)     

# 후위 순회 ( 왼, 오, 루트 순으로 방문)
def postorder(node):
    if node is None:
        return
    postorder(node.left) # none 뜰 때 까지 끝ㄱ가지 내려감
    postorder(node.right)
    print(node.key)

postorder(root)
