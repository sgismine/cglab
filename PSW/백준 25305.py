n,k = map(int,input().split())     # 응시자수, 상받는 사람 수 각각 
score = list(map(int,input().split()))  # 스코어 각각 공백을 기준으로 나누기

score.sort(reverse=True) #내림차순 정렬
print(score[k-1]) # 커트라인 출력 -1 하는 이유는 0부터 리스트가 시작하기 때문
 