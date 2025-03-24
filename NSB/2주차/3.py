# 백준 18870번

import sys

N = map(int,sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))
ans = []
X_tmp = X.copy()
X_tmp = set(X_tmp)
X_tmp = list(X_tmp)
X_tmp.sort()

l=len(X_tmp)

for i in X:
    for j in range(l):
        if i == X_tmp[j] :
            ans.append(j)

print(*ans)

# 시간초과 ..
"""
import sys

N = map(int,sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))
ans = []
X_tmp = sorted(set(X))


dic = {}
for i in range(len(X_tmp)) : 
    dic[X_tmp[i]] = i


l=len(X_tmp)


for i in X:
    print(dic[i],end=" ")

"""
