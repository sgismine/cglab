import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    tmp = sys.stdin.readline()
    lst.append(tmp)

lst = list(set(lst))

lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)