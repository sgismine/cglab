import sys

N = int(input())
ary = []
for i in range(N) :
    ary.append(int(sys.stdin.readline()))

ary.sort()

for i in ary:
    print(i)

