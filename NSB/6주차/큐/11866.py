# 11866 2번
import sys
N, K = map(int,sys.stdin.readline().split())

queue = list(range(1,N+1))
Josephus = []
cnt = 0
while(len(queue)>0):
    cnt += 1

    if cnt % K == 0 :
        Josephus.append(queue.pop(0))
    else :
        queue.append(queue.pop(0))

# 출력 양식 말고는 어려움 없었음    
print("<%s>"%(', '.join(map(str,Josephus))))
