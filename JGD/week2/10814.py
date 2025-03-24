import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    tmp = list(sys.stdin.readline().split())
    lst.append(tmp)

for i in range(n):
    lst[i][0] = int(lst[i][0])

lst.sort(key= lambda x:x[0])

print(lst)
