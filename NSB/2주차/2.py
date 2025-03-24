# 백준 10814번
import sys
mem =[]
N= int(input())

mem=[list(sys.stdin.readline().split()) for _ in range(N)]
for i in range(N):
    mem[i][0]=int(mem[i][0])
    mem[i].append(i)

mem = sorted(mem, key=lambda x:(x[0],x[2]))

for i in range(N) :
    print(mem[i][0], mem[i][1])