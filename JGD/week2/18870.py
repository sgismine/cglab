import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

sorted_lst = list(set(lst))
sorted_lst.sort()

for i in range(n):
    print(sorted_lst.index(lst[i]),end=" ")