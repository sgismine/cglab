n = int(input())  

list = []

for i in range(n):
    [a, b] = map(int, input().split())
    list.append([a, b])
    
list.sort()  #리스트 순서 대로 오름차순 정렬

for i in list:
    print(i[0], i[1])
    
