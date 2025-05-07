# 보자마자 생각난 코드 
# 그냥 pow쓰면 되는데?
# 시간 제한 짧아서 당연히 시간 초과 걸릴 줄 알았는데 왜 되지 이거 ?
import sys

a,b,c = map(int,sys.stdin.readline().split())

# 파이썬 내장함수 사용
print(pow(a,b,c))

# 분할정복으로 해보기
# 분할 정복에서의 거듭제곱 
# -> a^b = a^(b/2) * a^(b/2) (b가 짝수)
#    a^b = a^(b/2) * a^(b/2) *a (b가 홀수)
def check(a,b,c):
    if b ==1 :
        return a%c
    
    if b%2 == 0:
        return (check(a,b//2,c)**2)%c
    else:
        return (check(a,b//2,c)**2)*a%c


print(check(a,b,c))