# 백준 1181번

N=int(input())
word = [input() for _ in range(N)]
    
word = sorted(word, key=lambda x:(len(x),x))

print(word[0]) 
for i in range(1,N) :
    if word[i] != word[i-1] :
        print(word[i])