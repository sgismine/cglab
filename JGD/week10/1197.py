# MST : 크루스칼 or 프림을 사용. 크루스칼이 구현이 더 간단함
# union find : 사이클 판별에 사용, 사이클이 생기면-> 무시, 사이클이 없으면 간선 연결

import sys 
input = sys.stdin.readline

def find(parent,x): #유니온 파인드를 위한 부모 찾기
    if parent[x] != x:
        parent[x] = find(parent,parent[x]) # 경로 압축
    return parent[x]

# 유니온 연산
def union(parent,a,b):
    a_root = find(parent,a)
    b_root = find(parent,b)
    if a_root != b_root:
        parent[b_root] = a_root #b를 a에 흡수, 바꿔도 상관 x

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, weight = map(int, input().split())
    edges.append((a, b, weight))  

edges.sort(key=lambda x: x[2]) # weight 기준으로 정렬

parent = [i for i in range(V + 1)]  # 1번부터 V번까지, 자기 자신이 부모

result = 0
for weight, a, b in edges:
    if find(parent, a) != find(parent, b):  # 사이클이 생기지 않는다면
        union(parent, a, b) #a,b를 합치고(부모를 바꿔줌)
        result += weight

print(result)


