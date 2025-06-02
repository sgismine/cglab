#N = list(map(int,input().split()))
N = list(map(int, str(input()))) # 공백 없이 입력하므로 숫자를 문자로 받아서 int형으로 변환 

N.sort(reverse=True) #내림차순 정렬

for i in N :
    print(i, end='')  # 띄어쓰기 없이 출력