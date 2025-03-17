list = []

for i in range(5) :
    N = int(input())
    list.append(N)
    
list.sort()


print(int(sum(list)/5))    # 평균 구하기 평균이 자연수라고 했으므로 int적어주기
print(list[2]) # [0] ~ [4] 이 순으로 중앙값이 [2]          