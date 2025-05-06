# 11401 이항 계수
# 페르마의 소정리가 뭔데여
# 진짜 하나도 이해 안돼여

N, K = map(int,input().split())
P = 1000000007

def factorial(n):
    result = 1
    for i in range(2,n+1):
        result = result * i % P
    return result

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k//2)
    if k % 2:
        return tmp * tmp * n % P
    else:
        return tmp * tmp % P

ans = factorial(N) * square((factorial(N-K) * factorial(K) % P), P-2) % P
print(ans)