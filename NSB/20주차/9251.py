# 9251 LCS

import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

l1 = len(word1)
l2 = len(word2)

cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))

